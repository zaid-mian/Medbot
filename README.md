# MediBot - HTML/CSS/JS Version

A medical assistant chatbot with AI-powered symptom analysis and health guidance, specifically tailored for Pakistan. This version features a modern HTML/CSS/JavaScript frontend with the same robust Flask backend and database functionality.

## Features

### Frontend (HTML/CSS/JS)
- **Modern UI Design**: Beautiful gradient background with glassmorphism effects
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Chat Interface**: Smooth chat experience with typing indicators
- **Enhanced Styling**: Professional medical-themed design with animations
- **Accessibility**: Proper contrast ratios and keyboard navigation support

### Backend (Flask API)
- **AI-Powered Responses**: Integration with Google Gemini AI for medical advice
- **Pakistan-Specific Data**: Local hospital and medicine databases
- **Medical Context**: Tailored responses for Pakistani healthcare system
- **CORS Support**: Cross-origin requests enabled for frontend-backend communication
- **Database Integration**: SQLite database for user data and chat history

### Medical Capabilities
- **Symptom Analysis**: Comprehensive symptom evaluation and preliminary diagnosis
- **Medicine Recommendations**: Local Pakistani medicine brands and availability
- **Hospital Finder**: Location-based hospital recommendations
- **Emergency Contacts**: Pakistan emergency services (1122) integration
- **Safety Disclaimers**: Proper medical disclaimers and professional consultation advice

## Project Structure

```
medbot-html-version/
├── src/
│   ├── static/
│   │   ├── index.html          # Main HTML frontend
│   │   └── favicon.ico         # Website icon
│   ├── routes/
│   │   ├── chat.py            # Chat API endpoints
│   │   ├── medical.py         # Medical data endpoints
│   │   └── user.py            # User management endpoints
│   ├── data/
│   │   ├── hospitals.py       # Hospital data processor
│   │   ├── medicines.py       # Medicine data processor
│   │   ├── pakistan_hospitals_details.csv
│   │   └── Pakistan_Pharmaceutical_Products_Pricing_and_Availability_Data.xlsx
│   ├── models/
│   │   └── user.py            # Database models
│   ├── database/
│   │   └── app.db             # SQLite database (auto-created)
│   └── main.py                # Flask application setup
├── requirements.txt           # Python dependencies
├── run_app.py                # Application entry point
└── README.md                 # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install Additional Required Packages
```bash
pip install flask-cors flask-sqlalchemy google-generativeai pandas openpyxl
```

### Step 3: Run the Application
```bash
python run_app.py
```

The application will start on `http://127.0.0.1:5001`

## Configuration

### API Keys
The application uses Google Gemini AI. The API key is currently hardcoded in `src/routes/chat.py`. For production use, consider using environment variables:

```python
import os
API_KEY = os.getenv('GEMINI_API_KEY', 'your-default-key')
```

### Database
The SQLite database is automatically created in `src/database/app.db` when the application starts.

## API Endpoints

### Chat Endpoints
- `POST /api/chat` - Send message to AI assistant
- `GET /api/chat/health` - Health check for chat service

### Medical Data Endpoints
- `POST /api/medical/hospitals/search` - Search hospitals
- `GET /api/medical/hospitals/cities` - Get available cities
- `POST /api/medical/medicines/search` - Search medicines
- `GET /api/medical/medicines/info/<medicine_name>` - Get medicine details
- `GET /api/medical/medicines/companies` - Get pharmaceutical companies
- `GET /api/medical/health` - Health check for medical services

## Frontend Features

### Chat Interface
- **Auto-resizing Input**: Text area automatically adjusts to content
- **Typing Indicators**: Visual feedback during AI processing
- **Message Formatting**: Support for markdown-style formatting in responses
- **Timestamp Display**: Real-time timestamps for all messages
- **Error Handling**: Graceful error messages for connection issues

### Responsive Design
- **Mobile-First**: Optimized for mobile devices
- **Tablet Support**: Adapted layout for tablet screens
- **Desktop Enhancement**: Full-featured desktop experience
- **Touch-Friendly**: Large touch targets for mobile interaction

### Accessibility
- **Keyboard Navigation**: Full keyboard support
- **Screen Reader Friendly**: Proper ARIA labels and semantic HTML
- **High Contrast**: Accessible color combinations
- **Focus Management**: Clear focus indicators

## Customization

### Styling
The CSS is embedded in the HTML file for simplicity. Key customization areas:

- **Colors**: Modify the gradient backgrounds and accent colors
- **Typography**: Change font families and sizes
- **Layout**: Adjust container sizes and spacing
- **Animations**: Modify or disable animations

### Location Settings
The default location is set to Faisalabad, Pakistan. To change:

```javascript
function getCurrentLocation() {
    return {
        latitude: YOUR_LATITUDE,
        longitude: YOUR_LONGITUDE,
        city: 'YOUR_CITY'
    };
}
```

## Deployment

### Local Development
The application runs on `http://127.0.0.1:5001` by default.

### Production Deployment
For production deployment:

1. **Use a Production WSGI Server**: Replace the development server with Gunicorn or uWSGI
2. **Environment Variables**: Move sensitive data to environment variables
3. **Database**: Consider upgrading to PostgreSQL or MySQL for production
4. **Static Files**: Serve static files through a web server like Nginx
5. **HTTPS**: Enable SSL/TLS encryption

### Docker Deployment (Optional)
Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python", "run_app.py"]
```

## Comparison with Original

### Improvements Over Original
1. **Enhanced UI/UX**: More modern and professional design
2. **Better Responsiveness**: Improved mobile and tablet experience
3. **Smoother Animations**: Enhanced visual feedback and transitions
4. **Better Error Handling**: More robust error messages and recovery
5. **Improved Accessibility**: Better screen reader and keyboard support

### Maintained Features
1. **Same Backend Logic**: Identical API functionality and database structure
2. **AI Integration**: Same Google Gemini AI integration
3. **Medical Data**: Same hospital and medicine databases
4. **Pakistan Focus**: Same local context and emergency information

## Troubleshooting

### Common Issues

1. **Module Not Found Errors**
   ```bash
   pip install flask-cors flask-sqlalchemy google-generativeai
   ```

2. **Port Already in Use**
   - Change the port in `run_app.py`: `app.run(host='0.0.0.0', port=5002)`

3. **Database Issues**
   - Delete `src/database/app.db` to reset the database

4. **API Key Issues**
   - Ensure the Google Gemini API key is valid and has sufficient quota

### Performance Tips
- **Caching**: Implement response caching for frequently asked questions
- **Database Optimization**: Add indexes for frequently queried fields
- **Static File Serving**: Use a CDN or web server for static files in production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes. Please ensure compliance with medical regulations and data privacy laws in your jurisdiction.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Test with the health check endpoints
4. Verify all dependencies are installed correctly

## Acknowledgments

- Google Gemini AI for natural language processing
- Pakistan healthcare data providers
- Flask and related libraries for the backend framework
- Modern web standards for the frontend implementation

