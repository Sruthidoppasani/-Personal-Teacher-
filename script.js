const emojis = ["🧬", "📘", "🪐", "🔬", "🧠", "✨", "📚", "🧪"];
const container = document.querySelector('.emoji-container');


for (let i = 0; i < 30; i++) {
  const emoji = document.createElement('span');
  emoji.classList.add('emoji');
  emoji.textContent = emojis[Math.floor(Math.random() * emojis.length)];

  // Random positions and speed
  const x = Math.random() * 100 + 'vw';
  const y = Math.random() * 100 + 'vh';
  const duration = 10 + Math.random() * 10;

  emoji.style.setProperty('--x', x);
  emoji.style.setProperty('--y', y);
  emoji.style.animationDuration = `${duration}s`;

  container.appendChild(emoji);
}
