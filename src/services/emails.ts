const nodemailer = require('nodemailer');
const config = require('../config.json').emailing;

export default class Emails {
  transporter: any = null;

  constructor() {
    const transportConfig: any = Object.assign({
      port: 465,
      secure: true
    }, config);
    this.transporter = nodemailer.createTransport(transportConfig);
  }

  getCreationEmail(email: string): any {
    return {
      from: `"Marvel Reading Stats" <${config.from}>`,
      to: email,
      subject: 'Welcome to MRS',
      html: `
        <h1>Welcome on Marvel Reading Stats !</h1>
        <p>
          Your account form ${email} has been created.
          In order to log in, you can click on the link bellow.
        </p>
        <br/>
        <p>If you didn't asked to create an account for MRS platform,
        please ignore this email as the loggin link will expire in 15 minutes.</p>
        <br/>
        <p>Have a marvelous day !</p>
      `
    };
  }

  sendEmail(emailOptions: any): Promise<any> {
    return this.transporter.verify()
      .then(() => this.transporter.sendMail(emailOptions))
      .catch((err: any) => err);
  }

  notifyUserCreation(email: string) {
     const emailOptions:any = this.getCreationEmail(email);
     return this.sendEmail(emailOptions);
  }
}
