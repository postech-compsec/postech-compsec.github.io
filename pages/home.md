---
## Computer Security Lab @POSTECH
layout: default
title: Computer Security Lab @POSTECH
header: none
permalink: /
home_images:
  - src: "/assets/gallery/20250918-01.jpg"
    alt: "2025.09.18 Group Photo"
  - src: "/assets/gallery/20250918-02.jpg"
    alt: "2025.09.18 Group Photo"
  - src: "/assets/gallery/20250918-03.jpg"
    alt: "2025.09.18 Group Photo"
  - src: "/assets/gallery/20241121-01.jpg"
    alt: "2024.11.21 Group Photo"
---

![CompSec Logo](/assets/logo/compsec-main.png)
<br>

<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    {% for image in page.home_images %}
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="{{ forloop.index0 }}"
        {% if forloop.first %}class="active" aria-current="true"{% endif %}
        aria-label="Slide {{ forloop.index }}"
      ></button>
    {% endfor %}
  </div>

  <div class="carousel-inner">
    {% for image in page.home_images %}
      <div class="carousel-item {% if forloop.first %}active{% endif %}">
        <img src="{{ image.src | relative_url }}" class="d-block w-100" alt="{{ image.alt }}">
      </div>
    {% endfor %}
  </div>

  <!-- uncomment below if you want prev/next buttons -->
  <!--
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button> -->
</div>

## Computer Security Lab at POSTECH

> "Practical cyber-physical security:
> We hack, we patch, we secure real-world systems."

Our research group focuses on addressing **cybersecurity challenges**
across diverse interdisciplinary domains.
Our primary goal is to enhance the security and robustness
of a wide spectrum of computer systems,
ranging from `traditional software` and `operating systems`
to emerging systems such as
`Cyber-Physical Systems` (e.g., drones, autonomous vehicles, satellite systems)
and `Artificial Intelligence systems`.

Our research methodology encompasses various approaches,
including, but not limited to:
1. Developing automated methodologies for scalable bug identification.
2. Exploring offensive techniques to diagnose vulnerabilities in
existing systems.
3. Engineering secure and robust systems.

Ultimately, our overarching goal is to make practical impacts on
the cyber-physical safety of individuals who rely on computer-based systems
in their daily lives.

**NOTE:** If you are interested in working with us,
      please contact [Seulbae](mailto:seulbae@postech.ac.kr)
      with your **CV**, **transcript**, and details about the projects or ideas
      you would like to work on.

## News

- **<tt>[2025/12/02]</tt>** 🏆 Chiheon, Minki, Jangseop, and Junwoong won a "Special Award" (KIISC President's Award) at <a href="https://acdc.ai.kr/">2025 ACDC</a> Finals as Team RHCP!
- **<tt>[2025/11/01]</tt>** 🏆 Team RHCP (Chiheon, Minki, Jangseop, and Junwoong) advances to the <a href="https://acdc.ai.kr/">2025 ACDC</a> Finals!
- **<tt>[2025/09/01]</tt>** Minki, Jangseop, and Junwoong have started a Ph.D. program. Jimin and Jaehwan joined as undergrad interns. Welcome aboard!
- **<tt>[2025/08/10]</tt>** Team Cold Fusion placed 10th at DEF CON 33 CTF Finals!
- **<tt>[2025/06/16]</tt>** Woocheol and Gunha have joined CompSec Lab as undergrad interns. Welcome aboard!
- **<tt>[2025/04/14]</tt>** 🏆 Chiheon, Taeyeon, Kyungmin, Jaeyoung, and Jaewon advances to the <a href="https://defcon.org/html/defcon-33/dc-33-index.html">DEF CON 33 CTF Finals</a> as members of team Cold Fusion!
- **<tt>[2025/03/05]</tt>** Junwoong have joined CompSec Lab as a visiting undergrad intern. Welcome aboard!
- **<tt>[2025/02/17]</tt>** Jaewon have joined CompSec Lab as an undergrad intern. Welcome aboard!
- **<tt>[2025/02/17]</tt>** Chiheon has started an M.S. program. Welcome aboard!
- **<tt>[2025/01/06]</tt>** Jangseop, Kyungmin, Dongwan, Hanbi, Hyunsoo, and Jaeyoung have joined CompSec Lab. as undergrad interns. Welcome aboard!
- **<tt>[2024/10/30]</tt>** 🏆 Chiheon, Minki, Kihyun, and Taeyeon won a "Tech Award"
    (한국드론혁신협회장상) at <a href="http://www.hackthedrone.org/index.php">Hack the DRONE 2024</a> Finals as Team CompSec!
- **<tt>[2024/09/30]</tt>** Taeyeon have joined CompSec Lab as an undergrad intern. Welcome aboard!
- **<tt>[2024/09/08]</tt>** 🏆 Team CompSec (Chiheon, Minki, Kihyun, and Taeyeon)
    advances to the <a href="http://www.hackthedrone.org/index.php">Hack the DRONE 2024</a> Finals!
- **<tt>[2024/08/23]</tt>** Jongsoo have joined CompSec Lab. Welcome aboard!
- **<tt>[2024/08/11]</tt>** 🏆 Chiheon achieved 9th place as team Cold Fusion at the
    <a href="https://defcon.org/html/defcon-32/dc-32-index.html">DEF CON 32 CTF Finals</a>!
- **<tt>[2024/06/24]</tt>** Jeongwon and Minki have joined CompSec Lab. as visiting undergrad interns. Welcome aboard!
- **<tt>[2024/06/17]</tt>** Chiheon, Selim, Kihyun, and Young Seo have joined CompSec Lab. as undergrad interns. Welcome aboard!
- **<tt>[2024/02/01]</tt>** Computer Security Lab @POSTECH is established!

<!-- - [Installation]({{ '/docs/installation/' | relative_url }}) -->
<!-- - [Configuration]({{ '/docs/configuration/' | relative_url }}) -->
<!-- - [Markdown]({{ '/docs/markdown/' | relative_url }}) -->
