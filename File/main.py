<!DOCTYPE html>
<html>
<head>
  <title>Best Mobile App</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
      background: #111;
      color: #fff;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
    }

    .loader {
      font-size: 20px;
      margin-bottom: 10px;
      text-align: center;
    }

    .timer {
      font-size: 48px;
      font-weight: bold;
      color: #ff3333;
      animation: pulse 1s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.2); opacity: 0.7; }
      100% { transform: scale(1); opacity: 1; }
    }

    iframe {
      display: none;
      width: 100%;
      height: 100%;
      border: none;
      position: absolute;
      top: 0;
      left: 0;
    }
  </style>
</head>
<body>

<div class="loader">Loading... Please Wait</div>
<div class="timer" id="countdown">1</div>

<script>
  const countdownEl = document.getElementById("countdown");
  let count = 1;

  // Timer will keep increasing every second until iframe loads
  const interval = setInterval(() => {
    count++;
    countdownEl.textContent = count;
  }, 1000);

  const backupURL = "https://raw.githubusercontent.com/BIDDLG/The-Blogger-Files/main/demoxyz.txt";

  fetch(backupURL)
    .then(res => res.text())
    .then(url => {
      const iframe = document.createElement("iframe");
      iframe.src = url.trim();

      // Jab iframe load complete ho jaye
      iframe.onload = () => {
        clearInterval(interval);
        document.querySelector(".loader").style.display = "none";
        document.querySelector(".timer").style.display = "none";
        iframe.style.display = "block";
      };

      document.body.appendChild(iframe);
    })
    .catch(err => {
      document.body.innerHTML = "<h2 style='text-align:center;margin-top:20px;'>❌ Failed to load site</h2>";
      console.error("Error loading URL:", err);
    });
</script>

</body>
</html>
