const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Navigate to the Twitter page
  await page.goto('https://twitter.com/sQuelly620/status/1782931005633900994');

  // Extract links from the page
  const links = await page.evaluate(() => {
    const links = [];
    document.querySelectorAll('a').forEach(link => {
      links.push(link.href);
    });
    return links;
  });

  // Output the extracted links
  console.log('Extracted links:');
  console.log(links);

  // Simulate clicking on each link and observe behavior
  for (const link of links) {
    console.log('Clicking on:', link);
    await page.goto(link);
    // You can observe behavior here, such as checking for errors or analyzing the resulting page
    console.log('Page title:', await page.title());
    // Wait for a moment before proceeding to the next link
    await page.waitForTimeout(2000);
  }

  await browser.close();
})();
