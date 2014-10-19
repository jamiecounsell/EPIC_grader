from epic_audio import playSound
import os.path

DEFAULT_SOUNDFILE = "audio/error.wav"

class Error():
	def __init__(self, code, desc, soundfile=DEFAULT_SOUNDFILE):
		# Error Code
		self.code = code

		# Error Description
		self.description = desc

		# Optional sound file for error, else default
		self.sound = soundfile

	def alert(self):
		if os.path.isfile(self.sound):
			# Sound file found. Play sound.
			playSound(self.sound)
		else:
			# No sound file or file not found
			pass

NO_STUDENT_NO = Error("001", "You must enter a student number.")
BAD_STUDENT_NO = Error("002", "Student with this student number not found.")