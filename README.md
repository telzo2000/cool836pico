# cool836pico

# Note
cool836picoを完成したので、忘備録として記入します。
<br>
cool836picoは、m.kiが設計したキーボードです。<br>
cool836Aをベースにして、従来のpro microから、Raspberry pi pico（以下、ピコ）を採用し、敗戦処理等を新規設計したものである。<br>
特徴は、前述のピコを採用したこと。<br>
cool836Aと同じ、アリス配列をもしたキーレイアウトであること。<br>
スイッチソケットを採用して、Cherry MXとxkailh chocの両方が使えること。<br>
これら３点が挙げられる。<br>
基板の設計は、kicadで行った。すでにピコのfootprintを作った人がいたので、それを使った。
キーレイアウトは、cool836Aと同じため、前に使ったレイアウトのjsonファイルを再利用した。
配線処理は、cool836Aが最初にSU120を使ったものであったときの名残りで、colとrowは６x６であった。
この点を改善しようと思い、１２x３に変更した。その分、配線処理は簡易となったと思う。<br>
ピコはpro microと違い、基板本体にリセットスイッチを持っている。そのため、基板への設置面に制約がある。
なるべく、チップ類が露出しない方が良いと考えて、PCBに切り込みを入れる形にした。
マックエイトのスプリングピンヘッダを使用する限り、あまり関係ない仕様かもしれない。
一般的なピンヘッダでハンダ付けをした場合、この仕様は生きてくると思う。<br>
ネジ穴の位置は、外装となるアクリルプレートを考慮して配置した。ただし、二種類の高低差のあるスイッチが使用できるため、それに合わせたスイッチプレートの形状とした。
結果として、ピコのカバー部分のアクリルプレートを２種類用意することで解決した。<br>
これまでのcool836Aのような形状では難しくなり、菱形のような形状となった。今後、ピコの設置の場所について、洗練できれば、形状の見直しも視野に入れようと思う。<br>
ファームウェアについては、python系のkmk_firmwarexとrubyのprk_firmwareの２種類がある。両方試してみた。
どちらにもいえることが、pro microで使うqmk_firmwareよりも多分、作りやすいと思う。
逆にどちらもコンパイルの場面がないので、エラー表示を見て一つ一つ直していくことができない。
原因を探るのが難しかった。<br>
最初に上手く行ったのは、prk_firmwareのほうだった。
しかし、この文章はkmk_firmwareを装備したcool836picoで入力している。<br>
今後、どちらが優位になるか、私にはわからない。<br>

