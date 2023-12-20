require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.AntiqueWhite
		@label1.Font = System::Drawing::Font.new("Poor Richard", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.BurlyWood
		@label1.Location = System::Drawing::Point.new(149, 37)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(370, 195)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.BurlyWood
		@button1.Font = System::Drawing::Font.new("Poor Richard", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.OldLace
		@button1.Location = System::Drawing::Point.new(56, 272)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(220, 116)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.BurlyWood
		@button2.Font = System::Drawing::Font.new("Poor Richard", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.OldLace
		@button2.Location = System::Drawing::Point.new(401, 272)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(220, 116)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.OldLace
		self.ClientSize = System::Drawing::Size.new(683, 433)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "myschedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "1. Web Design\n 2. Study Hall\n 3. Computer Programming\n 4. French\n 5. Wildlife Ecology\n 6. AP Lit\n 7. Symphonic Orchestra\n 8. Precalculus"

	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

