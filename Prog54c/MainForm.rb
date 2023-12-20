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
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.LightSlateGray
		@button1.Font = System::Drawing::Font.new("Tw Cen MT Condensed", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Lavender
		@button1.Location = System::Drawing::Point.new(40, 340)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(160, 71)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.LightSlateGray
		@button2.Font = System::Drawing::Font.new("Tw Cen MT Condensed", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Lavender
		@button2.Location = System::Drawing::Point.new(216, 340)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(160, 71)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.LightSlateGray
		@button3.Font = System::Drawing::Font.new("Tw Cen MT Condensed", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.Lavender
		@button3.Location = System::Drawing::Point.new(394, 340)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(160, 71)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("OCR A Extended", 8.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(216, 94)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(160, 19)
		@textBox1.TabIndex = 7
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.LightSteelBlue
		@label2.Font = System::Drawing::Font.new("Tw Cen MT Condensed", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::Color.MidnightBlue
		@label2.Location = System::Drawing::Point.new(40, 211)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(502, 42)
		@label2.TabIndex = 10
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.LightSteelBlue
		@label3.Font = System::Drawing::Font.new("Tw Cen MT Condensed", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::Color.MidnightBlue
		@label3.Location = System::Drawing::Point.new(40, 273)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(502, 42)
		@label3.TabIndex = 11
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Lavender
		self.ClientSize = System::Drawing::Size.new(584, 454)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
	end

	def Button1Click(sender, e)
		pi = float(3.14159)
		radius = float(@textBox1.Text)
		area = pi * radius**2
		area = round(area,3)
		circumference = 2 * pi * radius
		circumference = round(circumference,3)
		@label2.Text = "area: " + str(area)
		@label3.Text = "circumference: " + str(circumference)
		
		
	end

	def MainFormLoad(sender, e)
		
	end
end

