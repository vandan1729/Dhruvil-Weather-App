#!/bin/bash

echo "🚀 Setting up Gujarat Weather App..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Get a free API key from https://openweathermap.org/api"
echo "2. Set up MySQL database"
echo "3. Update the .env file with your credentials"
echo "4. Run: python main.py"
echo ""
echo "🌤️ Enjoy your weather app!"