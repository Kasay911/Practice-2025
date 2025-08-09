const slider = document.querySelector('.slider');
const images = document.querySelectorAll('.slider img');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const counter = document.querySelector('.counter');

let currentIndex = 0;
const totalImages = images.length;

function updateSlider() {
    images.forEach((img, index) => {
        img.classList.toggle('active', index === currentIndex);
    });
    counter.textContent = `Изображение ${currentIndex + 1} из ${totalImages}`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalImages) % totalImages;
    updateSlider();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalImages;
    updateSlider();
});

updateSlider(); // Инициализация