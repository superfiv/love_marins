let cart = [];

function addToCart(productName, productPrice) {
    const product = { name: productName, price: productPrice, quantity: 1 };
    const existingProductIndex = cart.findIndex(item => item.name === productName);

    if (existingProductIndex >= 0) {
        cart[existingProductIndex].quantity++;
    } else {
        cart.push(product);
    }

    updateCart();
}

function updateCart() {
    const cartItemsContainer = document.getElementById('cartItems');
    cartItemsContainer.innerHTML = '';

    let total = 0;

    cart.forEach(item => {
        total += item.price * item.quantity;
        const cartItem = document.createElement('div');
        cartItem.textContent = `${item.name} - ${item.quantity} шт. - ${item.price * item.quantity} Руб.`;
        cartItemsContainer.appendChild(cartItem);
    });

    document.getElementById('cartTotal').textContent = `Итого: ${total} Руб.`;
}