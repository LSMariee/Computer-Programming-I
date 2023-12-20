import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.IndianRed
		self._button1.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MistyRose
		self._button1.Location = System.Drawing.Point(24, 372)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 83)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.IndianRed
		self._button2.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MistyRose
		self._button2.Location = System.Drawing.Point(214, 372)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 83)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.IndianRed
		self._button3.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MistyRose
		self._button3.Location = System.Drawing.Point(403, 372)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 83)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(155, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(147, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MistyRose
		self._label1.Location = System.Drawing.Point(89, 266)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(422, 43)
		self._label1.TabIndex = 4
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MistyRose
		self.ClientSize = System.Drawing.Size(591, 467)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()