const API_BASE_URL = 'https://your-backend-api.com'; // Replace with your backend URL

// Upload Plant Photo
async function uploadPlantPhoto(formData) {
    try {
        const response = await fetch(`${API_BASE_URL}/upload`, {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error uploading plant photo:', error);
        return { message: 'Failed to upload photo. Please try again.' };
    }
}