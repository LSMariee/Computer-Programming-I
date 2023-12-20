import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(231, 58)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(112, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(59, 59)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(155, 19)
		self._label1.TabIndex = 1
		self._label1.Text = "Sales for the month:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(43, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(182, 19)
		self._label2.TabIndex = 2
		self._label2.Text = "Advance pay awarded:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(231, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(112, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(79, 145)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 19)
		self._label3.TabIndex = 4
		self._label3.Text = "Commission Rate:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(116, 190)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(109, 19)
		self._label4.TabIndex = 6
		self._label4.Text = "Commission:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("MS Reference Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(141, 228)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(73, 19)
		self._label5.TabIndex = 7
		self._label5.Text = "Net Pay:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label6.Location = System.Drawing.Point(231, 228)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(112, 18)
		self._label6.TabIndex = 9
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label7.Location = System.Drawing.Point(231, 190)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(112, 18)
		self._label7.TabIndex = 10
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label8.Location = System.Drawing.Point(231, 145)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(112, 18)
		self._label8.TabIndex = 11
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button1.Font = System.Drawing.Font("MS Reference Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(24, 294)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 27)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button2.Font = System.Drawing.Font("MS Reference Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(154, 294)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 27)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button3.Font = System.Drawing.Font("MS Reference Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(277, 294)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 27)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Honeydew
		self.ClientSize = System.Drawing.Size(406, 358)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "pg240comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		sales = float(self._textBox1.Text)
		advpay = float(self._textBox2.Text)
		commrate = 0
		if sales >= 0 and sales < 10000:
			commrate = 0.05
		elif sales >= 10000 and sales < 15000:
			commrate = 0.1
		elif sales >= 15000 and sales < 18000:
			commrate = 0.12
		elif sales >= 18000 and sales < 22000:
			commrate = 0.14
		elif sales >= 22000:
			commrate = 0.16
			
		commission = commrate * sales
		net = commission - advpay
		self._label8.Text = str(commrate) + "%"
		self._label7.Text = "$" + str(round(commission, 2))
		self._label6.Text = "$" + str(net)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label8.Text = ""
		self._label7.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()