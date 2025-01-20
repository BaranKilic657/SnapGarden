// Handle File Upload
document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('upload-form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const fileInput = document.getElementById('plant-photo');
            if (fileInput.files.length === 0) {
                alert('Please select a file to upload.');
                return;
            }

            const file = fileInput.files[0];

            // Check file size (example: 5MB limit)
            if (file.size > 5 * 1024 * 1024) {
                alert('File size exceeds the 5MB limit.');
                return;
            }

            const formData = new FormData();
            formData.append('plantPhoto', file);

            // Simulate API call
            const uploadResult = document.getElementById('upload-result');
            if (uploadResult) {
                uploadResult.innerHTML = '<p>Analyzing your plant...</p>';
            }

            try {
                // Simulate a delay for analysis
                setTimeout(() => {
                    if (uploadResult) {
                        uploadResult.innerHTML = `
                            <p><strong>Plant Name:</strong> Fiddle Leaf Fig</p>
                            <p><strong>Health Status:</strong> Healthy</p>
                        `;
                    }
                }, 2000);
            } catch (error) {
                console.error('Error during file upload:', error);
                alert('An error occurred while analyzing the file.');
            }
        });
    }

    // Redirect to the login page
    function redirectToLogin() {
        // Replace 'login.html' with the actual path to your login page
        window.location.href = 'login.html';
    }

    // Handle Contact Form Submission
    const contactForm = document.querySelector('.contact form');
    if (contactForm) {
        contactForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent the default form submission behavior

            // Get form data
            const name = contactForm.querySelector('input[type="text"]').value;
            const email = contactForm.querySelector('input[type="email"]').value;
            const message = contactForm.querySelector('textarea').value;

            // Simulate form submission (you can replace this with an API call)
            console.log('Form submitted:', { name, email, message });

            // Show a success message (you can customize this)
            alert('Thank you for contacting us! We will get back to you soon.');

            // Optionally, reset the form
            contactForm.reset();
        });
    }
});