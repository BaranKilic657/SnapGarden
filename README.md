This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

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
- **Frontend**: Built with JavaScript frameworks.

- **Used Templates**: https://themefisher.com/products/quixlab-bootstrap & https://themefisher.com/products/small-apps-bootstrap

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
