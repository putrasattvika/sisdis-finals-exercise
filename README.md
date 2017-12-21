![Alt text](lat-uas-sisdis17.jpg?raw=true "Title")

Dalam sistem ini, terdapat 2 buah node : node 1 dan node 2. Ada juga node 'relay' yang meng-intercept pesan yang dikirim dari N1 ke N2.

Jika N1 ingin mengirim pesan ke N2, pesan tersebut harus dilewatkan pada exchange yang berwarna orange, melewati relay yang kemudian akan memforward pesan tersebut ke exchange hijau, yang mana N2 akan menjadi subscriber dari exchange hijau tersebut. Rute yang sama berlaku jika N2 ingin mengirim pesan ke N1.

Node relay, bisa mengirim pesan langsung ke N1 dan N2 melalui exchange berwarna biru. N1 dan N2 DILARANG untuk saling langsung berkomunikasi via exchange biru (walaupun secara teknis ini memungkinkan). Dengan kata lain, exchange biru hanya digunakan untuk node relay untuk bertukar informasi dengan N1 dan/atau N2.
