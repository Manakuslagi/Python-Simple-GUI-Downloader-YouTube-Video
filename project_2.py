import PySimpleGUI as sg
import pytube
import youtube_dl

def mp4_menu():
	sg.theme('Dark Blue 3')

	layout = [ [sg.Text('Input url that you want to download : '), sg.InputText()],
			   [sg.Text('Input resolution to download : '), sg.InputText()],
			   [sg.Button('Download MP4', size=(70, 2), key='DMP4')]]

	window = sg.Window('YouTube Downloader', layout)

	while True:
		event, values = window.read()

		url = pytube.YouTube(values[0])

		if event == sg.WIN_CLOSED:
			break
		elif event == 'DMP4':
			video = url.streams.get_by_resolution(values[1])
			video.download("C:/Users/hp/Documents/Py Project")

		print(event, values)
	window.close()

def mp3_menu():
	sg.theme('Dark Blue 3')

	layout = [ [sg.Text('Input url that you want to download : '), sg.InputText()],
			   [sg.Button('Download MP3', size=(70, 2), key='DMP3')]]

	window = sg.Window('YouTube Downloader', layout)

	while True:
		event, values = window.read()

		info = youtube_dl.YoutubeDL().extract_info(url=values[0], download=False)
		filename = f"{info['title']}.mp3"
		options= {
	        'format':'bestaudio/best',
	        'keepvideo':False,
	        'outtmpl':filename,
	    }

		if event == sg.WIN_CLOSED:
			break
		elif event == 'DMP3':
			with youtube_dl.YoutubeDL(options) as ydl:
				ydl.download([info['webpage_url']])

		print(event, values)
	window.close()
def home():
	sg.theme('Dark Blue 3')

	layout = [ [sg.Text('YouTube Downloader MP4 and MP3', font=('Arial', 20))],
		[sg.Button('Download MP4', size=(50, 2), key='MP4')],
		[sg.Button('Download MP3', size=(50, 2), key='MP3')]]

	window = sg.Window('YouTube Downloader', layout)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		elif event == 'MP4':
			window.close()
			mp4_menu()
		elif event == 'MP3':
			window.close()
			mp3_menu()
	window.close()

home()