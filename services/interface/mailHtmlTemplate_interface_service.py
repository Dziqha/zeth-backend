
class HTMLMessageResetPasswordBuilder:
    def build_resetpassword_message(self, username, reset_password_link, email):
        return f"""
        <!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!--><!--<![endif]-->
	<style>
		* {{
			box-sizing: border-box;
		}}

		body {{
			margin: 0;
			padding: 0;
		}}

		a[x-apple-data-detectors] {{
			color: inherit !important;
			text-decoration: inherit !important;
		}}

		#MessageViewBody a {{
			color: inherit;
			text-decoration: none;
		}}

		p {{
			line-height: inherit
		}}

		.desktop_hide,
		.desktop_hide table {{
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}}

		.image_block img+div {{
			display: none;
		}}

		sup,
		sub {{
			font-size: 75%;
			line-height: 0;
		}}

		@media (max-width:520px) {{
			.desktop_hide table.icons-outer {{
				display: inline-table !important;
			}}

			.mobile_hide {{
				display: none;
			}}

			.row-content {{
				width: 100% !important;
			}}

			.stack .column {{
				width: 100%;
				display: block;
			}}

			.mobile_hide {{
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}}

			.desktop_hide,
			.desktop_hide table {{
				display: table !important;
				max-height: none !important;
			}}

			.row-2 .column-1 .block-1.heading_block h3,
			.row-2 .column-1 .block-8.heading_block h3,
			.row-2 .column-1 .block-9.heading_block h3 {{
				font-size: 30px !important;
			}}
		}}
	</style><!--[if mso ]><style>sup, sub {{ font-size: 100% !important; }} sup {{ mso-text-raise:10% }} sub {{ mso-text-raise:-10% }}</style> <![endif]-->
</head>

<body class="body" style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 500px; margin: 0 auto;" width="500">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; font-weight: 400; text-align: center;">
																<table class="icons-outer" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-table;">
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img class="icon" src="https://e60763ac0f.imgdist.com/pub/bfra/btt8qrkp/alw/tdi/x2z/ZETH%20TEAM%20%281%29.png" height="auto" width="144" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 500px; margin: 0 auto;" width="500">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 20px; padding-left: 20px; padding-right: 20px; padding-top: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 18px;"><strong><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Hi {username}!</span></strong></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #723fff; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">We received a request to reset your password for your account on <span style="word-break: break-word; color: #006bff;">{email}</span> If this was you, don't worry! Resetting your password is quick and easy.<strong></strong></span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;"><strong>Please click the button below to set a new password:&nbsp;</strong></span></h3>
															</td>
														</tr>
													</table>
													<table class="button_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:20px;text-align:center;">
																<div class="alignment" align="center"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href=`{reset_password_link}` style="height:40px;width:127px;v-text-anchor:middle;" arcsize="10%" stroke="false" fillcolor="#7747ff">
<w:anchorlock/>
<v:textbox inset="0px,0px,0px,0px">
<center dir="false" style="color:#ffffff;font-family:Arial, sans-serif;font-size:12px">
<![endif]--><a class="button" href=`{reset_password_link}` target="_blank" style="background-color:#7747ff;border-bottom:0px solid #7747FF;border-left:0px solid #7747FF;border-radius:4px;border-right:0px solid #7747FF;border-top:0px solid #7747FF;color:#ffffff;display:inline-block;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:12px;font-weight:400;mso-border-alt:none;padding-bottom:8px;padding-top:8px;text-align:center;text-decoration:none;width:auto;word-break:keep-all;"><span style="word-break: break-word; padding-left: 20px; padding-right: 20px; font-size: 12px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 24px;">Reset Password</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;"><strong>If the button doesn't work, please copy and paste the following link into your browser:&nbsp;</strong></span></h3>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-6" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#101112;direction:ltr;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:19.2px;">
																	<p style="margin: 0;"><span style="word-break: break-word; color: #006bff;">{reset_password_link}</span></p>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #723fff; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span style="word-break: break-word; color: #000000;">This link will remain valid for the next 24 hours. If you don’t reset your password within this time frame, you’ll need to request a new link. If you didn’t request this password reset, please ignore this email. Rest assured, your account is secure, and no changes will be made. If you have any questions or encounter any issues, feel free to contact our support team at <span style="word-break: break-word; color: #006bff;">support@zeth.biz.id</span></span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-8" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 18px;"><strong><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Thank You,</span></strong></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-9" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:30px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 200%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 30px;"><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Zeth Team</span></h3>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
        """
    
class HTMLMessageActiveAcountBuilder:
	def build_ActiveAcount(self, username, activation_link):
		with open('mail_templates/verification_email.html', 'r') as file:
			html_content = file.read()
        
		print(html_content)
		
		html_content = html_content.replace('%NAME%', username)
		html_content = html_content.replace('%VERIFICATION_LINK%', activation_link)
		
		return html_content

class HTMLMessageWarningBuilder:
        def build_warning(self, username):
                return f"""
<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!--><!--<![endif]-->
	<style>
		* {{
			box-sizing: border-box;
		}}

		body {{
			margin: 0;
			padding: 0;
		}}

		a[x-apple-data-detectors] {{
			color: inherit !important;
			text-decoration: inherit !important;
		}}

		#MessageViewBody a {{
			color: inherit;
			text-decoration: none;
		}}

		p {{
			line-height: inherit
		}}

		.desktop_hide,
		.desktop_hide table {{
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}}

		.image_block img+div {{
			display: none;
		}}

		sup,
		sub {{
			font-size: 75%;
			line-height: 0;
		}}

		@media (max-width:520px) {{
			.desktop_hide table.icons-outer {{
				display: inline-table !important;
			}}

			.mobile_hide {{
				display: none;
			}}

			.row-content {{
				width: 100% !important;
			}}

			.stack .column {{
				width: 100%;
				display: block;
			}}

			.mobile_hide {{
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}}

			.desktop_hide,
			.desktop_hide table {{
				display: table !important;
				max-height: none !important;
			}}

			.row-2 .column-1 .block-1.heading_block h3,
			.row-2 .column-1 .block-5.heading_block h3,
			.row-2 .column-1 .block-6.heading_block h3 {{
				font-size: 30px !important;
			}}
		}}
	</style><!--[if mso ]><style>sup, sub {{ font-size: 100% !important; }} sup {{ mso-text-raise:10% }} sub {{ mso-text-raise:-10% }}</style> <![endif]-->
</head>

<body class="body" style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 500px; margin: 0 auto;" width="500">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; font-weight: 400; text-align: center;">
																<table class="icons-outer" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-table;">
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img class="icon" src="https://e60763ac0f.imgdist.com/pub/bfra/btt8qrkp/alw/tdi/x2z/ZETH%20TEAM%20%281%29.png" height="auto" width="144" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 500px; margin: 0 auto;" width="500">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 20px; padding-left: 20px; padding-right: 20px; padding-top: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 18px;"><strong><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Hi {username}!</span></strong></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 200%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 24px;"><span style="word-break: break-word; color: #000000;">We are writing to inform you that we have identified activity on your account that violates the Terms of Service for Zeth. This incident occurred on December 24, 2024, and involves the upload of content that does not comply with our guidelines. As a result, we have issued a formal warning to your account. Please note that any further violations may result in restrictions or even the permanent suspension of your account. If you believe this warning was issued in error, you can contact our support team at</span> support@zeth.biz.id <span style="word-break: break-word; color: #000000;">and include the following reference number: <strong>#A123456</strong>.</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span style="word-break: break-word; color: #000000;">To avoid future incidents, we encourage you to review our Terms of Service here: <span style="word-break: break-word; color: #006bff;"><a rel="noopener" href="https://zeth.biz.id/terms-of-service" target="_new" style="text-decoration: underline; color: #7747FF;">https://zeth.biz.id/terms-of-service</a>.</span></span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; font-weight: 400; letter-spacing: normal; line-height: 180%; text-align: justify; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 21.6px;"><span style="word-break: break-word; color: #000000;">Thank you for your attention to this matter. Let’s work together to maintain a safe and respectful environment for all our users.</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 18px;"><strong><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Thank You,</span></strong></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:30px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #7747FF; direction: ltr; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: normal; line-height: 200%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 30px;"><span class="tinyMce-placeholder" style="word-break: break-word; color: #000000;">Zeth Team</span></h3>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
"""

with open('../../mail_templates/verify_email.html', 'r') as file:
	html_content = file.read()

print(html_content)