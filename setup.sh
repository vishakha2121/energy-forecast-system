


echo "⚡ Energy Forecast System Setup Script"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_message() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Check Python version
print_message "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
if [ -z "$python_version" ]; then
    print_error "Python 3 not found. Please install Python 3.10+"
    exit 1
fi
print_message "Python $python_version found"

# Check Node.js version
print_message "Checking Node.js version..."
if ! command -v node &> /dev/null; then
    print_error "Node.js not found. Please install Node.js 18+"
    exit 1
fi
node_version=$(node --version)
print_message "Node.js $node_version found"

# Create directory structure
print_message "Creating directory structure..."
mkdir -p backend/data/{raw,processed,models}
mkdir -p backend/notebooks
mkdir -p backend/tests
mkdir -p database/migrations
mkdir -p database/seeds
mkdir -p frontend/src/{components,pages,services,hooks,utils,styles}
mkdir -p scripts
mkdir -p docker
mkdir -p docs

# Setup backend
print_message "Setting up backend..."
cd backend

# Create virtual environment
print_message "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
print_message "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if not exists
if [ ! -f ".env" ]; then
    print_message "Creating .env file..."
    cat > .env << EOF
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///../database/energy_db.sqlite
DEBUG=True
EOF
    print_warning "Please add your Gemini API key to backend/.env"
fi

cd ..

# Setup frontend
print_message "Setting up frontend..."
cd frontend

# Install dependencies
print_message "Installing Node.js dependencies..."
npm install

# Create .env file if not exists
if [ ! -f ".env" ]; then
    print_message "Creating frontend .env file..."
    cat > .env << EOF
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_GEMINI_ENABLED=true
EOF
fi

cd ..

# Setup database
print_message "Setting up database..."
python3 -c "
import sqlite3
import os
os.makedirs('database', exist_ok=True)
conn = sqlite3.connect('database/energy_db.sqlite')
conn.close()
print('Database created successfully')
"

# Run migrations
print_message "Running database migrations..."
for migration in database/migrations/*.sql; do
    if [ -f "$migration" ]; then
        print_message "Running $(basename $migration)..."
        sqlite3 database/energy_db.sqlite < "$migration"
    fi
done

# Generate sample data
print_message "Generating sample data..."
python3 scripts/generate_sample_data.py

# Make scripts executable
chmod +x scripts/*.py
chmod +x setup.sh

print_message ""
print_message "=========================================="
print_message "✅ Setup Complete!"
print_message "=========================================="
print_message ""
print_message "Next steps:"
print_message "1. Add your Gemini API key to backend/.env"
print_message "2. Start backend: cd backend && source venv/bin/activate && python run.py"
print_message "3. Start frontend: cd frontend && npm run dev"
print_message "4. Open browser: http://localhost:5173"
print_message ""
print_message "Optional: Train ML models"
print_message "  python3 scripts/train_models.py"
print_message ""
print_message "For more information, check README.md"