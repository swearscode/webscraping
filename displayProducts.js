document.addEventListener("DOMContentLoaded", () => {
    // Fetch the JSON file
    fetch("Products.json")
      .then(response => response.json())
      .then(data => {
        const container = document.getElementById("product-container");
  
        // Loop through each product and create HTML elements
        data.forEach(product => {
          // Create a div for each product
          const productDiv = document.createElement("div");
          productDiv.classList.add("product");
  
          // Create and set the image element
        //   const img = document.createElement("img");
        //   img.src = product.image_url;
        //   img.alt = product.title;
        //   productDiv.appendChild(img);
  
          // Create and set the title element
          const title = document.createElement("h2");
          title.classList.add("product-title");
          title.textContent = product.title;
          productDiv.appendChild(title);
  
          // Create and set the price element
          const price = document.createElement("p");
          price.classList.add("product-price");
          price.textContent = `Price: ₹${product.price}`;
          productDiv.appendChild(price);
  
          // Append the product div to the container
          container.appendChild(productDiv);
        });
      })
      .catch(error => {
        console.error("Error loading JSON data:", error);
      });
  });
  