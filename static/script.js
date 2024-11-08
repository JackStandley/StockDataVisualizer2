document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/symbols')
        .then(response => response.json())
        .then(symbols => {
            const symbolSelect = document.getElementById('symbol');
            symbolSelect.innerHTML = '';
            symbols.forEach(symbol => {
                const option = document.createElement('option');
                option.value = symbol;
                option.textContent = symbol;
                symbolSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching symbols:', error);
            const symbolSelect = document.getElementById('symbol');
            symbolSelect.innerHTML = '<option value="">Failed to load symbols</option>';
        });
});
