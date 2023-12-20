require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.PaleVioletRed
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.LavenderBlush
		@button1.Location = System::Drawing::Point.new(32, 328)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(153, 77)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.MediumVioletRed
		@label1.Location = System::Drawing::Point.new(129, 56)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 1
		@label1.Text = "A:"
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::Color.MediumVioletRed
		@label2.Location = System::Drawing::Point.new(129, 94)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 2
		@label2.Text = "B:"
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(303, 103)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(215, 20)
		@textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(303, 59)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(215, 20)
		@textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(303, 141)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(215, 20)
		@textBox3.TabIndex = 5
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.PaleVioletRed
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.LavenderBlush
		@button2.Location = System::Drawing::Point.new(225, 328)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(153, 77)
		@button2.TabIndex = 6
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.PaleVioletRed
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.LavenderBlush
		@button3.Location = System::Drawing::Point.new(430, 328)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(153, 77)
		@button3.TabIndex = 7
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Pink
		@label3.Font = System::Drawing::Font.new("Modern No. 20", 14.249999, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::Color.MediumVioletRed
		@label3.Location = System::Drawing::Point.new(32, 216)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(551, 40)
		@label3.TabIndex = 8
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Pink
		@label4.Font = System::Drawing::Font.new("Modern No. 20", 14.249999, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::Color.MediumVioletRed
		@label4.Location = System::Drawing::Point.new(32, 271)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(551, 39)
		@label4.TabIndex = 9
		# 
		# label5
		# 
		@label5.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.ForeColor = System::Drawing::Color.MediumVioletRed
		@label5.Location = System::Drawing::Point.new(129, 132)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(100, 23)
		@label5.TabIndex = 10
		@label5.Text = "C:"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.LavenderBlush
		self.ClientSize = System::Drawing::Size.new(624, 448)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "prog58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text)
		B = int(@textBox2.Text)
		C = int(@textBox3.Text)
		posroot = (-B + ($math.sqrt(B**2 - 4 * (A * C)))) / (2 * A)
		negroot = (-B - ($math.sqrt(B**2 - 4 * (A * C)))) / (2 * A)
		@label3.Text = "posroot: " + str(posroot)
		@label4.Text = "negroot: " + str(negroot)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

