# Dream Interpretation AI 🌙

## Overview
Dream Interpretation is an AI-powered Flask application that provides instant dream analysis and interpretation using Google's Gemini AI model.

## Quick Start 🚀

```bash
# Pull the image
docker pull [YOUR_DOCKERHUB_USERNAME]/dream-interpretation:latest

# Run with your Google API key
docker run -d -p 3000:3000 -e GOOGLE_API_KEY=your_api_key [YOUR_DOCKERHUB_USERNAME]/dream-interpretation:latest
```

Visit `http://localhost:3000` in your browser.

## Features ✨
- Instant dream analysis and interpretation
- Powered by Google's Gemini AI
- Simple and intuitive web interface
- Secure API key handling
- Lightweight container

## Environment Variables 🔐
Required environment variables:
- `GOOGLE_API_KEY`: Your Google AI API key

## Ports 🔌
- Container exposes port `3000`

## Volumes 📁
No volumes required for basic operation.

## Health Check 🏥
The application includes a basic health check endpoint at `/`.

## Tags 🏷️
- `latest`: Most recent stable version
- `v1.0`: Initial release
- `stable`: Production-ready version

## Update Instructions 🔄

To update to the latest version:

```bash
# Pull the latest version
docker pull [YOUR_DOCKERHUB_USERNAME]/dream-interpretation:latest

# Stop the current container
docker stop $(docker ps -q --filter ancestor=[YOUR_DOCKERHUB_USERNAME]/dream-interpretation)

# Remove the old container
docker rm $(docker ps -aq --filter ancestor=[YOUR_DOCKERHUB_USERNAME]/dream-interpretation)

# Run the new version
docker run -d -p 3000:3000 -e GOOGLE_API_KEY=your_api_key [YOUR_DOCKERHUB_USERNAME]/dream-interpretation:latest
```

## Security 🔒
- Non-root user in container
- No sensitive data in image
- Regular security updates

## Support 💬
For issues and feature requests, please visit our [GitHub repository](https://github.com/Devehab/dream-interpretation).

## License 📄
MIT License - see LICENSE file for details
