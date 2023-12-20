﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(70, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(276, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of calories in the food:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(352, 63)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(70, 125)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(276, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Enter the number of fat grams in the food:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(70, 192)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(276, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Percantage of calories that come from fat:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(352, 125)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Thistle
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(40, 270)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 29)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Thistle
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(191, 270)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 29)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Thistle
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Black
		self._button3.Location = System.Drawing.Point(350, 270)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 29)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Location = System.Drawing.Point(350, 192)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 20)
		self._label4.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Ivory
		self.ClientSize = System.Drawing.Size(518, 337)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg268FatCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		cals = float(self._textBox1.Text)
		fat = float(self._textBox2.Text)
		fatcals = fat * 9
		dec = fatcals / cals
		percent = dec * 100
		
		if fat > cals:
			MessageBox.Show("Invalid amount")
		
		self._label4.Text = str(percent) + "%"

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		

	def Button3Click(self, sender, e):
		Application.Exit()