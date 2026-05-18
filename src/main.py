import flet as ft 
from download_handler import download

class MultiDL:

    def __init__(self, page: ft.Page):
        
        self.page = page
        self.page.title = "MultiDL"
        self.page.padding = 0
        self.page.spacing = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment =  ft.MainAxisAlignment.CENTER


        self.page.on_resize = self.window_resizer

        self.Build_UI()
        self.text_scale_size()
        self.page.update()

 

    def Build_UI(self):
        self.URL_Field = ft.TextField(hint_text= "https://example.com/video...",bgcolor = "gray", opacity=0.3, 
                                      col = {"xs": 10, "sm": 11, "md": 11}, 
                                      border_radius = 30, 
                                      border_color = "black", 
                                      )
        self.Download_logo = ft.IconButton (icon = ft.Icons.DOWNLOAD,
                                            col = {"xs": 2, "sm": 1, "md": 1}, 
                                            icon_color = "#FFFFFF", 
                                            style = ft.ButtonStyle( bgcolor="#7E15E1", shape=ft.CircleBorder()))

        self.first_row =  ft.ResponsiveRow( controls= [self.URL_Field, self.Download_logo], vertical_alignment= ft.CrossAxisAlignment.CENTER, 
                                           )

        self.dynamid_MultiDL_label = ft.Text (value = "Video Downloader", weight = "bold", color= "black")
        self.supported_text =  ft.Text (value= "───────Supported Platforms───────", color="black")
        

            
        self.tiktok_logo = ft.Image(src="assets/tiktok.png", width=20, height=20)
        self.insta_logo = ft.Image(src="assets/instagram.png", width=20, height=20)
        self.facebook_logo = ft.Image(src="assets/facebook.png", width=20, height=20)
        self.yt_logo = ft.Image(src="assets/yt.png", width=20, height=20)
        self.x_logo = ft.Image(src="assets/x.png", width=20, height=20)
        self.linkedin_logo = ft.Image(src="assets/linkedin.png", width=30, height=30, )
        self.twitch_logo = ft.Image(src="assets/twitch.png", width=30, height=30)
       
        
        self.supported_logos_row = ft.Row(
            controls=[self.tiktok_logo, self.insta_logo, self.facebook_logo, self.yt_logo, self.x_logo, self.linkedin_logo, self.twitch_logo, ],
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=5
        )

        #row for recently downloaded label & view all 
        self.recently_downloaded_label =ft.Text(value = "Recently downloaded", color = "black", col={"xs": 8, "sm": 9, "md": 9})
        self.view_all = ft.TextButton (content = "View all >", col={"xs": 4, "sm": 3 ,"md": 3},style= ft.ButtonStyle(color="black",), align= ft.Alignment.CENTER_RIGHT)
        self.r_v = ft.ResponsiveRow (controls= [self.recently_downloaded_label, self.view_all, ], vertical_alignment= ft.CrossAxisAlignment.CENTER) 



        # self.donwloads_column = ft.Column (
        #     spacing = 10, 
        #     scroll = ft.ScrollMode.AUTO
        # )

        self.recently_downloaded_container = ft.Container(
            bgcolor="#9D9D9D",
            opacity=0.5,
            border_radius= 30,
            expand= True, 
        
        )

        
        self.container_row = ft.ResponsiveRow(
            controls=[self.recently_downloaded_container],
            alignment=ft.MainAxisAlignment.CENTER,
            expand= True
        )
        


        self.download_button = ft.ElevatedButton(content="Download", icon= ft.Icons.DOWNLOAD)
            
        self.MainContainer = ft.Container(
            expand=True,
            padding= 20,
            

            image=ft.DecorationImage(
                src="background.png", 
                fit= ft.BoxFit.COVER    
            ),

            
            content = ft.Column(
                controls = [self.dynamid_MultiDL_label,
                            self.first_row, 
                            ft.Divider(height=10, thickness= 1, color="transparent"),
                            self.supported_text,
                            self.supported_logos_row, 
                            self.r_v,
                            self.container_row,
                            self.download_button],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                
                
            )
        )
                
        self.page.add(self.MainContainer
        )

    

    def handler(self, e):
        url = self.URL_Field.value
        download(url)

        


    def text_scale_size(self):
        current_size = self.page.width

        calculated_size = current_size * 0.04 #4% fo the screen width.

        if calculated_size < 18:
            self.dynamid_MultiDL_label.size = 18
            self.supported_text.size = 10
            self.recently_downloaded_label.size = 10
            self.view_all.size = 10
            
        elif calculated_size > 32:
            self.dynamid_MultiDL_label.size = 32
            self.supported_text.size = 15
            self.recently_downloaded_label.size =  15
            self.view_all.size = 18
            
        else:
            self.dynamid_MultiDL_label.size = calculated_size
            self.supported_text.size = 10
            self.recently_downloaded_label.size = 15
            self.view_all.size = 18
            

    
    def window_resizer (self, e):
        self.text_scale_size()
        self.dynamid_MultiDL_label.update()
        self.supported_text.update()
        self.recently_downloaded_label.update()
        self.recently_downloaded_container.update()

             

        
ft.app(target = MultiDL)