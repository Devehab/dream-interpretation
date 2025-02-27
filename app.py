from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

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
    
    prompt = create_prompt(dream_text, reference_source, language)
    
    try:
        response = model.generate_content(prompt)
        interpretation = response.text
        return jsonify({'success': True, 'interpretation': interpretation})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=3000)
