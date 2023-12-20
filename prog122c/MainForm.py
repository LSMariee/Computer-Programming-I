import math
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
		self._listBox1.BackColor = System.Drawing.Color.MediumSeaGreen
		self._listBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Honeydew
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(337, 340)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Honeydew
		self._button1.Location = System.Drawing.Point(14, 371)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(108, 51)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Honeydew
		self._button2.Location = System.Drawing.Point(128, 371)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 51)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Honeydew
		self._button3.Location = System.Drawing.Point(242, 371)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(108, 51)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Honeydew
		self.ClientSize = System.Drawing.Size(374, 464)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "num1\t\tnum2\t\tnum3\t\tnum4"
		for num in range(2, 11, 2):
			col1 = num
			col2 = num + 1
			col3 = num * 2
			col4 = num * num
			line = str(col1) + "\t" + str(col2) + "\t" + str(col3) + "\t" + str(col4)
			self._listBox1.Items.Add(line)
		
			

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()