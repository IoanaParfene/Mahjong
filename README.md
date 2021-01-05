# Mahjong
A GUI **Mahjong** implementation for the UAIC FII Python course.

## Game description
The **144** tiles are arranged in a special four-layer pattern with their faces upwards. A pair of tiles can be matched if they are available(there are **no neighbours** on **top** and either **left**, **right** or **both sides**) and have the **same pattern**. The game is over when all tiles are removed from the board.
![Game](https://user-images.githubusercontent.com/57050677/103654381-7a319a00-4f6e-11eb-9a8c-401a74e11625.jpg)

## Installation
1. Get **python** and **pip** from [here](https://www.python.org/downloads/).
2. Clone the repo to a local directory or download it as zip and un-zip it.
3. Open the project in [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows).
4. Import everything needed.
5. Navigate to **main.py** and press **Run**.

## Concept
In my **implementation** of the game, the number of tiles and the arrangement follow the **original model** described above. I used two pairs of 36 pieces.<br /> <br />

The player is allowed to use **3 hints**.<br />
<img src="https://user-images.githubusercontent.com/57050677/103658594-17430180-4f74-11eb-8176-d8f8b5e89bcc.jpg" width="600" height="400"><br /> <br />

The moves can be **undone 3 times**.<br />
<img src="https://user-images.githubusercontent.com/57050677/103658596-19a55b80-4f74-11eb-93e9-b0fe686a5833.jpg" width="600" height="400">
<img src="https://user-images.githubusercontent.com/57050677/103658599-1ad68880-4f74-11eb-9b2c-5837b27a2302.jpg" width="600" height="400"><br /> <br />

The tiles can be **shuffled 2 times**, as the player desires. <br />
<img src="https://user-images.githubusercontent.com/57050677/103658608-1c07b580-4f74-11eb-8cc6-c98c60c285cc.jpg" width="600" height="400">
<img src="https://user-images.githubusercontent.com/57050677/103658611-1ca04c00-4f74-11eb-9479-825252622081.jpg" width="600" height="400"><br /> <br />

If there are no moves left, the game **auto-shuffles** the tiles.  <br />
<img src="https://user-images.githubusercontent.com/57050677/103658612-1dd17900-4f74-11eb-8f2f-829792f6ee94.jpg" width="600" height="400">
<img src="https://user-images.githubusercontent.com/57050677/103658618-1f9b3c80-4f74-11eb-84a9-544e37e03ed9.jpg" width="600" height="400"> <br /> <br />

If there are **no moves** and **no shuffles** left, the game is **lost**.  <br />
<img src="https://user-images.githubusercontent.com/57050677/103658625-21fd9680-4f74-11eb-9940-678721f05f58.jpg" width="600" height="400"> <br /> <br />

If there are **no pieces** left on the board, the player **won**.  <br />
<img src="https://user-images.githubusercontent.com/57050677/103658634-245ff080-4f74-11eb-8189-dbe8a596b428.jpg" width="600" height="400"> <br /> <br />
                                                                                                       
The game can be **restarted** at any point. <br />
<img src="https://user-images.githubusercontent.com/57050677/103658640-25911d80-4f74-11eb-8cc0-948f8b9d41a1.jpg" width="600" height="400">
<img src="https://user-images.githubusercontent.com/57050677/103658644-2629b400-4f74-11eb-8d3b-b972591b6aed.jpg" width="600" height="400"> <br /> <br />

The **instructions** can be viewed at any time by hovering the **(i)** button. <br />
<img src="https://user-images.githubusercontent.com/57050677/103658648-26c24a80-4f74-11eb-83bf-00ac385a362b.jpg" width="600" height="400"> <br /> <br />

## Resources
* [Game Rules](https://en.wikipedia.org/wiki/Mahjong_solitaire)
* [Sound](https://www.looperman.com/loops/tags/free-chinese-loops-samples-sounds-wavs-download)
* [Tile Vector Art](https://www.vecteezy.com/members/laphotospot)
* [Vector Art Icons](https://www.flaticon.com/categories/arrows)
