// script.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');

    // Function to add a new filter field
    window.addFilterField = function() {
        const filterFieldsContainer = document.getElementById('filterFields');

        // Create new filter elements
        const filterNameSelect = document.createElement('select');
        filterNameSelect.name = `filter_name_${filterFieldsContainer.children.length}`;
        filterNameSelect.className = 'filterName';
        const optionIndustry = document.createElement('option');
        optionIndustry.value = 'industry';
        optionIndustry.text = 'Industry';
        const optionPeRatio = document.createElement('option');
        optionPeRatio.value = 'pe_ratio';
        optionPeRatio.text = 'PE Ratio';
        const optionBookValue = document.createElement('option');
        optionBookValue.value = 'book_value';
        optionBookValue.text = 'Book Value';
        filterNameSelect.appendChild(optionIndustry);
        filterNameSelect.appendChild(optionPeRatio);
        filterNameSelect.appendChild(optionBookValue);

        const filterMinInput = document.createElement('input');
        filterMinInput.type = 'number';
        filterMinInput.name = `filter_min_${filterFieldsContainer.children.length}`;
        filterMinInput.className = 'filterMin';

        const filterMaxInput = document.createElement('input');
        filterMaxInput.type = 'number';
        filterMaxInput.name = `filter_max_${filterFieldsContainer.children.length}`;
        filterMaxInput.className = 'filterMax';

        // Append new filter elements to the container
        filterFieldsContainer.appendChild(document.createElement('br'));
        filterFieldsContainer.appendChild(document.createTextNode('Filter Name: '));
        filterFieldsContainer.appendChild(filterNameSelect);
        filterFieldsContainer.appendChild(document.createElement('br'));
        filterFieldsContainer.appendChild(document.createTextNode('Min Value: '));
        filterFieldsContainer.appendChild(filterMinInput);
        filterFieldsContainer.appendChild(document.createTextNode('Max Value: '));
        filterFieldsContainer.appendChild(filterMaxInput);
        filterFieldsContainer.appendChild(document.createElement('br'));
    };
});
