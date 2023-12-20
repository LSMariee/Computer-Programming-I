import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(445, 355)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 385)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(136, 61)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(322, 385)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(136, 61)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(168, 385)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(136, 61)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(470, 458)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tCube Root\t\tCube"
		self._listBox1.Items.Add(heading)
		for num in range(-25, 25):
			col1 = num 
			col2 = -(-num) ** (1./3)
			col3 = num ** 3
			line = str(col1) + "/t/t" + str(col2) + "/t/t" + str(col3)
			self._listBox1.Items.Add(line)

	def Button3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass