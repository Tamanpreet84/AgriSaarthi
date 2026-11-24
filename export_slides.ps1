$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open('C:\Users\taman\OneDrive\Desktop\agrisaarthi\AgriSaarthi_Presentation.pptx', 1, 0, 0)
$pres.Slides.Item(1).Export('C:\Users\taman\OneDrive\Desktop\agrisaarthi\ppt_assets\slide1_rendered.png', 'PNG', 1920, 1080)
$pres.Slides.Item(8).Export('C:\Users\taman\OneDrive\Desktop\agrisaarthi\ppt_assets\slide8_rendered.png', 'PNG', 1920, 1080)
$pres.Slides.Item(12).Export('C:\Users\taman\OneDrive\Desktop\agrisaarthi\ppt_assets\slide12_rendered.png', 'PNG', 1920, 1080)
$pres.Close()
$ppt.Quit()
Write-Output "Export complete"
