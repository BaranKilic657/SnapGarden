
# SnapGarden 🌱  
**Effortless Plant Care, Powered by AI**  

SnapGarden is an AI-powered platform that simplifies plant care for both beginners and seasoned gardeners. With advanced features like plant identification, health analysis, and personalized watering schedules, SnapGarden makes maintaining your plants stress-free.

---

## Table of Contents  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features  
- **Plant Identification**: Simply snap a photo of your plant, and our AI will instantly identify it and provide customized care tips.
- **Health Analysis**: Upload a photo, and the AI will detect any signs of pests, diseases, or general poor health, offering actionable advice for recovery.
- **Watering Schedule**: Personalized reminders help you keep your plants hydrated with just the right amount of water, ensuring they thrive effortlessly.

---

## Installation  

### Prerequisites  
Before you start, make sure you have the following tools installed:  
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/get-started)
- [Conda](https://docs.conda.io/projects/conda/en/latest/user_guide/install/index.html)  

### 1. Clone the Repository  
Clone the SnapGarden repository to your local machine:  
```bash
git clone https://github.com/ge95bid/snapgarden.git
cd snapgarden
```

### 2. Setup the Database  
To run SnapGarden, you will need the database image. Load and start the database container with the following commands:

```bash
docker load -i obsidian-db.tar
docker run -d --name obsidian-db obsidian-db
```

This will set up the database required for SnapGarden to operate.

### 3. Setup the AI Model (LLM)  

#### 3.1 Clone the LLM Repository  
The platform uses the MiniCPM-V model for AI-powered features. Clone the repository and navigate to the source folder:

```bash
git clone https://github.com/OpenBMB/MiniCPM-V.git
cd MiniCPM-V
```

#### 3.2 Create and Activate the Conda Environment  
Create a new Conda environment for the project:

```bash
conda create -n MiniCPM-V python=3.10 -y
conda activate MiniCPM-V
```

#### 3.3 Install Dependencies  
Install all required Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage  

Once you've completed the installation, you can start using SnapGarden!  

- **Plant Identification**: Capture a photo of your plant through the app, and SnapGarden's AI will instantly identify it and offer care tips.
- **Health Analysis**: Upload photos of your plants to check for any issues like pests or disease. The AI will give detailed advice to help improve their health.
- **Watering Reminders**: The app will notify you when it's time to water your plants based on their individual needs.

---

## Technologies Used  

- **AI/ML Models**: MiniCPM-V for plant identification and health analysis.  
- **Backend**: Docker for containerization and PostgreSQL as the database.  
- **Frontend**: Built with modern JavaScript frameworks (React/Next.js).  
- **Cloud**: Deployment on cloud platforms like AWS or Azure (depending on user choice).

---

## Contributing  

We welcome contributions! If you'd like to contribute to SnapGarden, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

## License  

SnapGarden is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This version improves clarity and ensures that the installation process is laid out in a structured and easy-to-follow way. It also provides extra context where needed for the user to better understand each step.
