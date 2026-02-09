document.addEventListener("DOMContentLoaded", () => {
    const feed = document.getElementById("feed");

    fetch("/api/v1/posts/feed")
        .then(r => r.json())
        .then(data => {
            data.forEach(item => {
                if (item.is_ad) {
                    feed.innerHTML += `
                        <div class="ad-block">
                            <h3>${item.title}</h3>
                            ${item.image_url ? `<img src="${item.image_url}" class="ad-img">` : ""}
                            <a class="btn" href="${item.link}" target="_blank">Перейти</a>
                        </div>
                    `;
                } else {
                    feed.innerHTML += `
                        <div class="post">
                            <p>${item.content}</p>
                        </div>
                    `;
                }
            });
        });
});
