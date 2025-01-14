// Example: Render a simple calendar
function renderCalendar() {
    const calendar = document.getElementById('calendar');
    calendar.innerHTML = `
        <ul>
            <li>Monday: Water your Fiddle Leaf Fig</li>
            <li>Thursday: Fertilize your Snake Plant</li>
            <li>Saturday: Prune your Monstera</li>
        </ul>
    `;
}

// Initialize Calendar
document.addEventListener('DOMContentLoaded', renderCalendar);