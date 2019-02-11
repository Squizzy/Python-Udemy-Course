import webbrowser

# webbrowser.open("https://www.python.org", new=1)

# help(webbrowser)

# ### using arguments
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=";", end=" ")

### use another web brower

# opera = webbrowser.get(using='chrome')  # didn't work because the browser must be in the PATH
# opera.open_new("https://www.python.org")

opera = webbrowser.get('opera %s').open("https://www.python.org")
