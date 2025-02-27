from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure the Gemini API
api_key = os.getenv('GOOGLE_API_KEY')
logger.info(f"API Key length: {len(api_key) if api_key else 'None'}")
genai.configure(api_key=api_key)

# Use the correct model name
try:
    # List available models to debug
    models = genai.list_models()
    logger.info(f"Available models: {[model.name for model in models]}")
    
    # Use a specific Gemini model that we know works
    model_name = 'gemini-1.5-pro'
    logger.info(f"Using model: {model_name}")
    model = genai.GenerativeModel(model_name)
except Exception as e:
    logger.error(f"Error setting up model: {str(e)}", exc_info=True)
    # Try an alternative model if the first one fails
    try:
        model_name = 'gemini-1.5-flash'
        logger.info(f"Trying alternative model: {model_name}")
        model = genai.GenerativeModel(model_name)
    except Exception as e2:
        logger.error(f"Error with alternative model: {str(e2)}", exc_info=True)
        raise RuntimeError("Failed to initialize any Gemini model")

def create_prompt(dream_description, reference_source, language):
    base_prompt = {
        "en": f"""Analyze the following dream from an Islamic perspective using {reference_source}:
Dream: {dream_description}

Please provide:
1. Dream Type (Choose one):
   - Righteous Vision (Ru'ya)
   - Satanic Dream
   - Self-talking Dream
   - No Religious Interpretation
   Include a brief explanation of the chosen type.

2. Detailed Interpretation:
   - Main symbols and their meanings
   - Overall interpretation
   - Relevant references from the chosen source

3. Additional Context Needed (if any):
   - Emotional state
   - Physical condition
   - Environmental factors
   - Timing
   - Cultural context

4. Guidance and Recommendations:
   - Islamic perspective
   - Practical advice

Please format the response clearly and make it easy to understand.""",
        
        "ar": f"""حلل الحلم التالي من منظور إسلامي باستخدام {reference_source}:
الحلم: {dream_description}

يرجى تقديم:
1. نوع الحلم (اختر واحداً):
   - رؤيا صالحة
   - حلم من الشيطان
   - حديث نفس
   - ليس له تفسير ديني
   مع شرح مختصر للنوع المختار.

2. التفسير المفصل:
   - الرموز الرئيسية ومعانيها
   - التفسير الشامل
   - المراجع ذات الصلة من المصدر المختار

3. السياق الإضافي المطلوب (إن وجد):
   - الحالة النفسية
   - الحالة الجسدية
   - العوامل البيئية
   - التوقيت
   - السياق الثقافي

4. الإرشادات والتوصيات:
   - المنظور الإسلامي
   - نصائح عملية

يرجى تنسيق الرد بشكل واضح وسهل الفهم."""
    }
    
    return base_prompt[language]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/interpret', methods=['POST'])
def interpret_dream():
    data = request.json
    dream_text = data.get('dream')
    reference_source = data.get('reference')
    language = data.get('language', 'ar')
    
    logger.info(f"Received dream interpretation request: Language={language}, Reference={reference_source}")
    
    prompt = create_prompt(dream_text, reference_source, language)
    logger.info(f"Created prompt with length: {len(prompt)}")
    
    try:
        logger.info("Sending request to Gemini API")
        response = model.generate_content(prompt)
        interpretation = response.text
        logger.info("Successfully received interpretation from Gemini API")
        return jsonify({'success': True, 'interpretation': interpretation})
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error during interpretation: {error_msg}", exc_info=True)
        
        # Check for quota exceeded error
        if "429" in error_msg and "quota" in error_msg.lower():
            user_message = {
                "ar": "تم تجاوز حصة API. يرجى المحاولة لاحقًا أو استخدام مفتاح API آخر.",
                "en": "API quota exceeded. Please try again later or use a different API key."
            }
            return jsonify({
                'success': False, 
                'error': error_msg,
                'user_message': user_message[language]
            })
        
        # Try with a simpler prompt as a fallback
        try:
            logger.info("Trying with a simpler prompt")
            simple_prompt = f"Interpret this dream from an Islamic perspective: {dream_text}"
            response = model.generate_content(simple_prompt)
            interpretation = response.text
            logger.info("Successfully received interpretation with simpler prompt")
            return jsonify({'success': True, 'interpretation': interpretation})
        except Exception as e2:
            error_msg2 = str(e2)
            logger.error(f"Error with simpler prompt: {error_msg2}", exc_info=True)
            
            # Check for quota exceeded error in the fallback
            if "429" in error_msg2 and "quota" in error_msg2.lower():
                user_message = {
                    "ar": "تم تجاوز حصة API. يرجى المحاولة لاحقًا أو استخدام مفتاح API آخر.",
                    "en": "API quota exceeded. Please try again later or use a different API key."
                }
                return jsonify({
                    'success': False, 
                    'error': f"Original error: {error_msg}, Fallback error: {error_msg2}",
                    'user_message': user_message[language]
                })
            
            return jsonify({
                'success': False, 
                'error': f"Original error: {error_msg}, Fallback error: {error_msg2}"
            })

if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=3000)
