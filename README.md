
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
- [Miniconda](https://docs.anaconda.com/miniconda/install/) 
- For GPU:
   - NVIDIA GPU with Compute Capability ≥ 7.0 (T4/V100/A100 recommended)
   - NVIDIA Drivers ≥ 525.60.13
   - Linux recommended (Windows WSL2 supported)

### Environment Options

| Feature                | GPU Environment                 | CPU Environment                 |
|------------------------|---------------------------------|---------------------------------|
| Target Hardware        | NVIDIA GPUs (T4/V100/A100)      | CPUs                            |
| PyTorch                | CUDA 12.1 builds                | CPU-only builds                 |
| TensorFlow             | GPU-accelerated                 | CPU-only                        |
| JAX                    | CUDA/CUDNN support              | CPU-only                        |
| RAM                    | ~8GB                            | ~8GB                            |
| Disk Space             | ~15GB                           | ~15GB                           |



### 1. Clone the Repository  
Clone the SnapGarden repository to your local machine:  
```bash
git clone https://github.com/ge95bid/snapgarden.git
cd snapgarden
```

### 2. Setup
Create a conda environment depending on required configuration and limits.

**For GPU**
```bash
conda env create -f environment_gpu.yaml
conda activate SnapGarden_GPU
```

**For CPU**
```bash
conda env create -f environment_cpu.yaml
conda activate SnapGarden_CPU
```

## Startup

Multiple terminals are required to run this project

1. **Start the LLM Backend** 

```bash
cd Backend
uvicorn main:app --reload
```

2. **Start the Authentication Backend**

```bash
cd Backend
python server.py
```

3. **Start the Website Frontend**

```bash
cd Frontend
python -m http.server 8001
```

---

## Usage  

Once you've completed the installation, you can start using SnapGarden!  

- **Plant Identification**: Capture a photo of your plant through the app, and SnapGarden's AI will instantly identify it and offer care tips.
- **Health Analysis**: Upload photos of your plants to check for any issues like pests or disease. The AI will give detailed advice to help improve their health.
- **Watering Reminders**: The app will notify you when it's time to water your plants based on their individual needs.

---

## Technologies Used  

- **AI/ML Models**: Salesforce/blip2-opt-2.7b for plant identification and health analysis.  
- **Backend**: Built with Python.
- **Frontend**: Built with JavaScript frameworks. Used Template: https://themefisher.com/products/quixlab-bootstrap

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
