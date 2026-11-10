const rankInput = document.querySelector('#rank-input');
const rankPreview = document.querySelector('.rank-preview');
const heroRank = document.querySelector('#hero-rank');
const predictForm = document.querySelector('#predict-form');
const submitButton = document.querySelector('#submit-button');

if (rankInput && rankPreview) {
  const formatRank = () => {
    const rank = Number(rankInput.value);
    const formattedRank = rank > 0 ? new Intl.NumberFormat('en-IN').format(rank) : '—';
    rankPreview.textContent = formattedRank;
    if (heroRank) heroRank.textContent = formattedRank;
  };

  rankInput.addEventListener('input', formatRank);
  formatRank();
}

if (predictForm && submitButton) {
  predictForm.addEventListener('submit', () => {
    submitButton.disabled = true;
    submitButton.setAttribute('aria-busy', 'true');
    submitButton.querySelector('span:first-child').textContent = 'Finding your options…';
  });
}

