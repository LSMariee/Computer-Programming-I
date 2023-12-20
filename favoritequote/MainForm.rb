require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.PaleGoldenrod
		@button1.Font = System::Drawing::Font.new("Microsoft Himalaya", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Olive
		@button1.Location = System::Drawing::Point.new(89, 255)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(200, 108)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.PaleGoldenrod
		@button2.Font = System::Drawing::Font.new("Microsoft Himalaya", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Olive
		@button2.Location = System::Drawing::Point.new(416, 255)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(200, 108)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.DarkKhaki
		@label1.Font = System::Drawing::Font.new("Microsoft Himalaya", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.LightGoldenrodYellow
		@label1.Location = System::Drawing::Point.new(179, 55)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(360, 141)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Beige
		self.ClientSize = System::Drawing::Size.new(713, 406)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "favoritequote"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Changing is our normal state. Even if we're not changing on the outside, we're changing on the inside constantly."
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

