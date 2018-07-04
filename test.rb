system "python3 test.py http://www.topstarnews.net/news/photo/201804/388535_33701_1249.jpg"
system "convert -fill none -fuzz 5% -draw 'matte 0,0 floodfill' output.png real_output.png"