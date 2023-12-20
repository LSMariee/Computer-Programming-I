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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(85, 68)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(107, 20)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(198, 67)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(132, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(198, 131)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(132, 20)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(42, 131)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(150, 20)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(42, 193)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 20)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary per pay period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(198, 193)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(132, 20)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SandyBrown
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(147, 264)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 25)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Moccasin
		self.ClientSize = System.Drawing.Size(408, 319)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg153salarycalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		annsalary = float(self._textBox1.Text)
		ppyr = float(self._textBox2.Text)
		salarypp = annsalary / ppyr
		self._label4.Text = "$" + str(round(salarypp, 2))