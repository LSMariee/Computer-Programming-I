import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumAquamarine
		self._label1.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(68, 41)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(321, 190)
		self._label1.TabIndex = 0
		self._label1.Text = "Quantity Sold"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumAquamarine
		self._label2.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(118, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Package A:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(240, 89)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumAquamarine
		self._label3.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(118, 136)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Package B:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumAquamarine
		self._label4.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(118, 183)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Package C:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(240, 139)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(240, 186)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MediumSeaGreen
		self._label5.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(21, 256)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(218, 161)
		self._label5.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.Font = System.Drawing.Font("Myanmar Text", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(295, 305)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 34)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkCyan
		self._button2.Font = System.Drawing.Font("Myanmar Text", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(242, 345)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 37)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkCyan
		self._button3.Font = System.Drawing.Font("Myanmar Text", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(345, 345)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 37)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Azure
		self.ClientSize = System.Drawing.Size(444, 447)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg269SoftwareSales"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pkgA = int(self._textBox1.Text)
		pkgB = int(self._textBox2.Text)
		pkgC = int(self._textBox3.Text)
		
		if pkgA >= 10 and pkgA <= 19:
			discA = (99 * pkgA) * 0.2
			priceA = (99 * pkgA) - discA
		elif pkgA >= 20 and pkgA <= 49:
			discA = (99 * pkgA) * 0.3
			priceA = (99 * pkgA) - discA
		elif pkgA >= 50 and pkgA <= 99:
			discA = (99 * pkgA) * 0.4
			priceA = (99 * pkgA) - discA
		elif pkgA >= 100:
			discA = (99 * pkgA) * 0.5
			priceA = (99 * pkgA) - discA
		else:
			discA = (99 * pkgA) + 0
			priceA = discA
			
		if pkgB >= 10 and pkgB <= 19:
			discB = (199 * pkgB) * 0.2
			priceB = (199 * pkgB) - discB
		elif pkgB >= 20 and pkgB <= 49:
			discB = (199 * pkgB) * 0.3
			priceB = (199 * pkgB) - discB
		elif pkgB >= 50 and pkgB <= 99:
			discB = (199 * pkgB) * 0.4
			priceB = (199 * pkgB) - discB
		elif pkgB >= 100:
			discB = (199 * pkgB) * 0.5
			priceB = (199 * pkgB) - discB
		else:
			discB = (199 * pkgB) + 0
			priceB = discB
			
		if pkgC >= 10 and pkgC <= 19:
			discC = (299 * pkgC) * 0.2
			priceC = (299 * pkgC) - discC
		elif pkgC >= 20 and pkgC <= 49:
			discC = (299 * pkgC) * 0.3
			priceC = (299 * pkgC) - discC
		elif pkgC >= 50 and pkgC <= 99:
			discC = (299 * pkgC) * 0.4
			priceC = (299 * pkgC) - discC
		elif pkgC >= 100:
			discC = (299 * pkgC) * 0.5
			priceC = (299 * pkgC) - discC
		else:
			discC = (299 * pkgC) + 0
			priceC = discC
		
		total = priceA + priceB + priceC
		
		self._label5.Text = "Package A: $" + str(priceA) + "\nPackage B: $" + str(priceB) + "\nPackage C: $" + str(priceC) + "\nGrand Total: $" + str(total)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()