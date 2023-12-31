﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(267, 84)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(270, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(267, 161)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(270, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.SeaGreen
		self._label1.Location = System.Drawing.Point(70, 84)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(182, 38)
		self._label1.TabIndex = 2
		self._label1.Text = "Speed Limit:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.SeaGreen
		self._label2.Location = System.Drawing.Point(43, 156)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(200, 38)
		self._label2.TabIndex = 3
		self._label2.Text = "Vehicle Speed:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Honeydew
		self._label3.Location = System.Drawing.Point(267, 235)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(270, 38)
		self._label3.TabIndex = 4
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.SeaGreen
		self._label4.Location = System.Drawing.Point(156, 235)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(96, 38)
		self._label4.TabIndex = 5
		self._label4.Text = "Fine:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Honeydew
		self._button1.Location = System.Drawing.Point(34, 375)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(166, 75)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Honeydew
		self._button2.Location = System.Drawing.Point(220, 375)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(166, 75)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Honeydew
		self._button3.Location = System.Drawing.Point(409, 375)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(166, 75)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Honeydew
		self.ClientSize = System.Drawing.Size(599, 473)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		limit = int(self._textBox1.Text)
		spd = int(self._textBox2.Text)
		numover = spd - limit
		fine = 5 * numover + 20
		self._label3.Text = str(fine)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()