import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(112, 88)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(129, 20)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter a number:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(275, 88)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(115, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Honeydew
		self._button1.Location = System.Drawing.Point(55, 272)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 44)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Honeydew
		self._button2.Location = System.Drawing.Point(190, 272)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 44)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Honeydew
		self._button3.Location = System.Drawing.Point(324, 272)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 44)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SeaGreen
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Honeydew
		self._label2.Location = System.Drawing.Point(112, 150)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(278, 31)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Honeydew
		self.ClientSize = System.Drawing.Size(498, 418)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		factorial = math.factorial(num)
		if num == 0:
			self._label2.Text = ""
		else:
			self._label2.Text = "the value of " + str(num) + "! is " + str(factorial)

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()