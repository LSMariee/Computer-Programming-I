import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleVioletRed
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.LavenderBlush
		self._button1.Location = System.Drawing.Point(46, 319)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(167, 81)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LavenderBlush
		self._label1.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label1.Location = System.Drawing.Point(68, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(145, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "A:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(263, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(261, 20)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.LavenderBlush
		self._button2.Location = System.Drawing.Point(241, 319)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(167, 81)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleVioletRed
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.LavenderBlush
		self._button3.Location = System.Drawing.Point(434, 319)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(167, 81)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(263, 85)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(261, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(263, 138)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(261, 20)
		self._textBox3.TabIndex = 6
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LavenderBlush
		self._label2.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label2.Location = System.Drawing.Point(68, 85)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(145, 23)
		self._label2.TabIndex = 7
		self._label2.Text = "B:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LavenderBlush
		self._label3.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label3.Location = System.Drawing.Point(68, 138)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(145, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "C:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label4.Location = System.Drawing.Point(46, 203)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(555, 33)
		self._label4.TabIndex = 9
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Pink
		self._label5.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label5.Location = System.Drawing.Point(46, 260)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(555, 33)
		self._label5.TabIndex = 10
		self._label5.Text = "label5"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LavenderBlush
		self.ClientSize = System.Drawing.Size(639, 444)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = int(@textBox1.Text)
		b = int(@textBox2.Text)
		c = int(@textbox2.Text)
		posroot = (-b+$math.sqrt(...))
		negroot = (-b-$math.sqrt(...))
		pass

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass