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
		self._listBox1.BackColor = System.Drawing.Color.SandyBrown
		self._listBox1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.SeaShell
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 16
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(492, 324)
		self._listBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SandyBrown
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.SeaShell
		self._button1.Location = System.Drawing.Point(12, 382)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 59)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SandyBrown
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SeaShell
		self._button2.Location = System.Drawing.Point(181, 382)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(149, 59)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SandyBrown
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.SeaShell
		self._button3.Location = System.Drawing.Point(355, 382)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(149, 59)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.NavajoWhite
		self.ClientSize = System.Drawing.Size(519, 471)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\tSquare\tSquare Root\tCube\t4th Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 20+1):
			col1 = num
			col2 = num**2
			col3 = num**0.5
			col4 = num**3
			col5 = num**0.25
			line = str(col1) + "\t" + str(col2) + "\t" + str(round(col3, 4)) + "\t\t" + str(round(col4, 4)) + "\t" + str(round(col5, 4))
			self._listBox1.Items.Add(line)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()