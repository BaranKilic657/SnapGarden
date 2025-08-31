import Image from "next/image";

export default function Page() {
  return (
    <div>
      {/* Basic Page Needs */}
      <meta charSet="utf-8" />
      <title>SnapGarden | Your Garden Assistant</title>
      {/* Mobile Specific Metas */}
      <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
      <meta
        name="description"
        content="SnapGarden - AI-powered plant care assistant"
      />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0, maximum-scale=5.0"
      />
      {/* theme meta */}
      <meta name="theme-name" content="snapgarden" />
      {/* Favicon */}
      <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png" />
      {/* PLUGINS CSS STYLE */}
      <link rel="stylesheet" href="plugins/bootstrap/bootstrap.min.css" />
      <link rel="stylesheet" href="plugins/themify-icons/themify-icons.css" />
      <link rel="stylesheet" href="plugins/slick/slick.css" />
      <link rel="stylesheet" href="plugins/slick/slick-theme.css" />
      <link rel="stylesheet" href="plugins/fancybox/jquery.fancybox.min.css" />
      <link rel="stylesheet" href="plugins/aos/aos.css" />
      {/* CUSTOM CSS */}
      <link href="css/style.css" rel="stylesheet" />
      <nav className="navbar main-nav navbar-expand-lg px-2 px-sm-0 py-2 py-lg-0">
        <div className="container">
          <a className="navbar-brand" href="index.html">
            <img src="images/logo.png" alt="logo" />
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="ti-menu" />
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item active">
                <a className="nav-link" href="index.html">
                  Home
                </a>
              </li>
              <li className="nav-item dropdown @@pages">
                <a
                  className="nav-link dropdown-toggle"
                  href="#"
                  data-toggle="dropdown"
                >
                  Pages
                  <span>
                    <i className="ti-angle-down" />
                  </span>
                </a>
                {/* Dropdown list */}
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item @@about" href="about.html">
                      About
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item @@faq" href="FAQ.html">
                      FAQ
                    </a>
                  </li>
                </ul>
              </li>
              <li className="nav-item @@contact">
                <a className="nav-link" href="contact.html">
                  Contact
                </a>
              </li>
              <li className="nav-item @@signin">
                <a className="nav-link sign-in-btn" href="sign-in.html">
                  Sign In
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      {/*====================================
=            Hero Section            =
=====================================*/}
      <section className="section gradient-banner">
        <div className="shapes-container">
          <div
            className="shape"
            data-aos="fade-down-left"
            data-aos-duration={1500}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="fade-down"
            data-aos-duration={1000}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="fade-up-right"
            data-aos-duration={1000}
            data-aos-delay={200}
          />
          <div
            className="shape"
            data-aos="fade-up"
            data-aos-duration={1000}
            data-aos-delay={200}
          />
          <div
            className="shape"
            data-aos="fade-down-left"
            data-aos-duration={1000}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="fade-down-left"
            data-aos-duration={1000}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="zoom-in"
            data-aos-duration={1000}
            data-aos-delay={300}
          />
          <div
            className="shape"
            data-aos="fade-down-right"
            data-aos-duration={500}
            data-aos-delay={200}
          />
          <div
            className="shape"
            data-aos="fade-down-right"
            data-aos-duration={500}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="zoom-out"
            data-aos-duration={2000}
            data-aos-delay={500}
          />
          <div
            className="shape"
            data-aos="fade-up-right"
            data-aos-duration={500}
            data-aos-delay={200}
          />
          <div
            className="shape"
            data-aos="fade-down-left"
            data-aos-duration={500}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="fade-up"
            data-aos-duration={500}
            data-aos-delay={0}
          />
          <div
            className="shape"
            data-aos="fade-down"
            data-aos-duration={500}
            data-aos-delay={0}
          />
          <div
            className="shape"
            data-aos="fade-up-right"
            data-aos-duration={500}
            data-aos-delay={100}
          />
          <div
            className="shape"
            data-aos="fade-down-left"
            data-aos-duration={500}
            data-aos-delay={0}
          />
        </div>
        <div className="container">
          <div className="row align-items-center">
            <div className="col-md-6 order-2 order-md-1 text-center text-md-left">
              <h1 className="text-white font-weight-bold mb-4">
                {" "}
                Your Garden Assistant, One Snap Away
              </h1>
              <p className="text-white mb-5">
                Your plants deserve the best care — let SnapGarden make it
                effortless.
              </p>
              <a href="sign-up.html" className="btn btn-main-md">
                Try out now!
              </a>
            </div>
            <div className="col-md-6 text-center order-1 order-md-2">
              <img
                className="img-fluid"
                src="images/mobile.png"
                alt="screenshot"
              />
            </div>
          </div>
        </div>
      </section>
      {/*====  End of Hero Section  ====*/}
      <section className="section pt-0 position-relative pull-top">
        <div className="container">
          <div className="rounded shadow p-5 bg-white">
            <div className="row">
              <div className="col-lg-4 col-md-6 mt-5 mt-md-0 text-center">
                <i
                  className="ti-shine"
                  style={{ color: "#027340", fontSize: "3rem" }}
                />
                <h3 className="mt-4 text-capitalize h5">
                  Plant Identification
                </h3>
                <p className="regular text-muted">
                  Snap a photo, and our AI instantly identifies your plant and
                  provides tailored care tips.
                </p>
              </div>
              <div className="col-lg-4 col-md-6 mt-5 mt-md-0 text-center">
                <i
                  className="ti-heart"
                  style={{ color: "#027340", fontSize: "3rem" }}
                />
                <h3 className="mt-4 text-capitalize h5">Health Analysis</h3>
                <p className="regular text-muted">
                  Detect signs of pests, diseases, or poor health with a quick
                  photo analysis and get actionable advice.
                </p>
              </div>
              <div className="col-lg-4 col-md-12 mt-5 mt-lg-0 text-center">
                <i
                  className="ti-paint-bucket"
                  style={{ color: "#027340", fontSize: "3rem" }}
                />
                <h3 className="mt-4 text-capitalize h5">Watering Schedule</h3>
                <p className="regular text-muted">
                  Get personalized watering reminders to keep your plants
                  hydrated and thriving effortlessly.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
      {/*==================================
=            Feature Grid            =
===================================*/}
      <section className="feature section pt-0">
        <div className="container">
          <div className="row">
            <div className="col-lg-6 ml-auto justify-content-center">
              {/* Feature Mockup */}
              <div className="image-content" data-aos="fade-right">
                <img
                  className="img-fluid"
                  src="images/feature-new-01.png"
                  alt="iphone"
                />
              </div>
            </div>
            <div className="col-lg-6 mr-auto align-self-center">
              <div className="feature-content">
                {/* Feature Title */}
                <h2>Plants Deserve the Best Care!</h2>
                {/* Feature Description */}
                <p className="desc">
                  At SnapGarden, we believe every plant deserves to thrive.
                  That’s why we’ve created an AI-powered platform to help you
                  give your plants the care they need, when they need it. From
                  instant identification and personalized watering schedules to
                  health monitoring and expert advice, SnapGarden is your
                  trusted companion for growing happy, healthy plants.
                </p>
              </div>
              {/* Testimonial Quote */}
              <div className="testimonial">
                <p>
                  "At SnapGarden, our mission is to empower plant lovers with
                  the tools they need to nurture their greenery effortlessly. By
                  combining cutting-edge AI with an intuitive design, we’re
                  making plant care accessible, sustainable, and enjoyable for
                  everyone."
                </p>
                <ul className="list-inline meta">
                  <li className="list-inline-item">
                    <img
                      src="images/testimonial/feature-testimonial-thumb.jpg"
                      alt="Test"
                    />
                  </li>
                  <li className="list-inline-item">
                    Kenny Nguyen, CEO of SnapGarden
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
      {/*====  End of Feature Grid  ====*/}
      {/*==============================
=            Services            =
===============================*/}
      <section className="service section bg-gray">
        <div className="container-fluid p-0">
          <div className="row">
            <div className="col-lg-12">
              <div className="section-title">
                <h2>Simple, Smart, and Green-Friendly</h2>
                <p>
                  Our user-friendly interface is designed to make plant care
                  intuitive—bringing expert guidance to your fingertips with
                  just a few taps. 🌿
                </p>
              </div>
            </div>
          </div>

          <div className="row g-0">
            {/* no-gutters -> g-0 in BS5 */}
            <div className="col-lg-6 align-self-center d-flex justify-content-end">
              {/* Feature Image */}
              <div
                className="service-thumb left fit-content"
                data-aos="fade-right"
              >
                <Image
                  src="/images/feature/iphone-ipad.jpg"
                  alt="iphone-ipad"
                  className=""
                  width={773}
                  height={390}
                />
              </div>
            </div>

            <div className="col-lg-5 align-self-center">
              <div className="service-box">
                <div className="row align-items-center">
                  <div className="col-md-6 col-12">
                    {/* col-xs-12 -> col-12 */}
                    <div className="service-item">
                      {/* Icon (Themify) */}
                      <i className="ti-heart" />
                      <h3>Effortless Plant Care</h3>
                      <p>
                        SnapGarden simplifies plant care with AI-powered tools,
                        making it accessible for everyone...
                      </p>
                    </div>
                  </div>

                  <div className="col-md-6 col-12">
                    <div className="service-item">
                      <i className="ti-time" />
                      <h3>Time-Saving</h3>
                      <p>
                        With instant plant identification, health analysis, and
                        personalized watering schedules...
                      </p>
                    </div>
                  </div>

                  <div className="col-md-6 col-12">
                    <div className="service-item">
                      <i className="ti-reload" />
                      <h3>Promotes Sustainability</h3>
                      <p>
                        By helping users care for their plants effectively,
                        SnapGarden encourages greener living...
                      </p>
                    </div>
                  </div>

                  <div className="col-md-6 col-12">
                    <div className="service-item">
                      <i className="ti-cloud-up" />
                      <h3>Innovative and Intuitive</h3>
                      <p>
                        The combination of cutting-edge AI technology and a
                        user-friendly interface makes SnapGarden unique...
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      {/*====  End of Services  ====*/}
      {/*=================================
=            Video Promo            =
==================================*/}
      <section className="video-promo section bg-1">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="content-block">
                {/* Heading */}
                <h2>Watch Our Promo Video</h2>
                {/* Promotional Speech */}
                <p>
                  See how SnapGarden makes plant care effortless with AI-powered
                  tools and a user-friendly interface.
                </p>
                {/* Popup Video */}
                <a
                  data-fancybox
                  href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                >
                  <i className="ti-control-play video" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="call-to-action-app section bg-blue">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <h2>It’s time to nurture your plants like never before!</h2>
              <p>
                Join SnapGarden today and make plant care simple, smart, and
                stress-free!
              </p>
              <ul className="list-inline">
                <li className="list-inline-item">
                  <a href="sign-in.html" className="btn btn-rounded-icon">
                    Try out now!
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>
      {/*============================
=            Footer            =
=============================*/}
      <footer>
        <div className="footer-main">
          <div className="container">
            <div className="row">
              <div className="col-lg-4 col-md-12 m-md-auto align-self-center">
                <div className="block">
                  <a href="index.html">
                    <img src="images/logo-alt.png" alt="footer-logo" />
                  </a>
                  {/* Social Site Icons */}
                  <ul className="social-icon list-inline">
                    <li className="list-inline-item">
                      <a href="https://www.facebook.com">
                        <i className="ti-facebook" />
                      </a>
                    </li>
                    <li className="list-inline-item">
                      <a href="https://twitter.com">
                        <i className="ti-twitter" />
                      </a>
                    </li>
                    <li className="list-inline-item">
                      <a href="https://www.instagram.com">
                        <i className="ti-instagram" />
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
              <div className="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
                <div className="block-2">
                  {/* heading */}
                  <h6>Product</h6>
                  {/* links */}
                  <ul>
                    <li>
                      <a href="FAQ.html">FAQs</a>
                    </li>
                  </ul>
                </div>
              </div>
              <div className="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
                <div className="block-2">
                  {/* heading */}
                  <h6>Resources</h6>
                  {/* links */}
                  <ul>
                    <li>
                      <a href="sign-up.html">Sign Up</a>
                    </li>
                    <li>
                      <a href="sign-in.html">Log In</a>
                    </li>
                  </ul>
                </div>
              </div>
              <div className="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
                <div className="block-2">
                  {/* heading */}
                  <h6>Company</h6>
                  {/* links */}
                  <ul>
                    <li>
                      <a href="about.html">About</a>
                    </li>
                    <li>
                      <a href="contact.html">Contact</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
      {/* To Top */}
      <div className="scroll-top-to">
        <i className="ti-angle-up" />
      </div>
      {/* JAVASCRIPTS */}
    </div>
  );
}
