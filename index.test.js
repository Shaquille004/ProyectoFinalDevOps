const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');


// Load the HTML file
const html = fs.readFileSync(path.resolve(__dirname, 'index.html'), 'utf8');

describe('index.html', () => {
    let dom;
    let document;

    beforeAll(() => {
        dom = new JSDOM(html);
        document = dom.window.document;
    });

    test('should have a title "Hola Mundo"', () => {
        const title = document.querySelector('title');
        expect(title).not.toBeNull();
        expect(title.textContent).toBe('Hola Mundo');
    });

    test('should have an h1 element with "Hola, Mundo!" text', () => {
        const h1 = document.querySelector('h1');
        expect(h1).not.toBeNull();
        expect(h1.textContent).toBe('Hola, Mundo!');
    });

    test('should have a paragraph welcoming the user', () => {
        const paragraph = document.querySelector('p');
        expect(paragraph).not.toBeNull();
        expect(paragraph.textContent).toContain('Bienvenido');
    });
    
});
