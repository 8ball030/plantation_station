const styles = {};

const Theme = styled.div`
 /* fonts */
  --font-inter: Inter;

  /* font sizes */
  --font-size-3xs: 10px;
  --font-size-sm: 14px;
  --font-size-mini: 15px;
  --font-size-lg: 18px;
  --font-size-xs: 12px;
  --font-size-base: 16px;
  --font-size-xl: 20px;
  --font-size-13xl: 32px;

  /* Colors */
  --color-gray-100: #272727;
  --color-gray-200: #171717;
  --color-gray-300: #151515;
  --color-gray-400: #111;
  --color-gray-500: rgba(255, 255, 255, 0.2);
  --color-white: #fff;
  --color-gainsboro: #d9d9d9;
  --color-dimgray: #666;
  --color-darkslategray-100: #313131;
  --color-darkslategray-200: #303030;
  --color-darkgray: #999;
  --color-whitesmoke: #ebebeb;
  --color-mediumspringgreen: #26ffb1;
  --color-black: #000;

  /* Gaps */
  --gap-13xl: 32px;
  --gap-5xl: 24px;
  --gap-xs: 12px;
  --gap-5xs: 8px;
  --gap-7xs: 6px;
  --gap-base: 16px;
  --gap-9xs: 4px;

  /* Paddings */
  --padding-21xl: 40px;
  --padding-13xl: 32px;
  --padding-53xl: 72px;
  --padding-37xl: 56px;
  --padding-base: 16px;
  --padding-5xs: 8px;
  --padding-xs: 12px;
  --padding-5xl: 24px;

  /* border radiuses */
  --br-5xl: 24px;
  --br-9xs: 4px;
  --br-base: 16px;
  --br-xs: 12px;
  --br-5xs: 8px;
  --br-11xl: 30px;

div {
  position: relative;
}
.badge {
  position: absolute;
  top: 207px;
  left: 441.5px;
  border-radius: var(--br-11xl);
  background-color: var(--color-mediumspringgreen);
  width: 24px;
  height: 24px;
  display: flex;
  flex-direction: column;
  padding: var(--padding-5xs);
  box-sizing: border-box;
  align-items: center;
  justify-content: center;
  font-size: var(--font-size-base);
  color: var(--color-black);
}
.frameChild {
  align-self: stretch;
  position: relative;
  border-radius: var(--br-5xl);
  width: 131px;
}
.plantName,
.showAll {
  position: relative;
  display: none;
}
.plantName {
  display: inline-block;
  width: 333px;
}
.frameIcon {
  position: relative;
  width: 20px;
  height: 20px;
  overflow: hidden;
  flex-shrink: 0;
}
.plantNameParent,
.x786c65d14c8d137c4b45a8a90d4c2Parent {
  display: flex;
  justify-content: flex-start;
  gap: var(--gap-xs);
}
.x786c65d14c8d137c4b45a8a90d4c2Parent {
  flex-direction: row;
  align-items: center;
  font-size: var(--font-size-xs);
  color: var(--color-dimgray);
}
.plantNameParent {
  flex-direction: column;
  align-items: flex-start;
  font-size: var(--font-size-base);
}
.growing {
  position: relative;
  font-weight: 500;
}
.growingWrapper {
  border-radius: var(--br-xs);
  background-color: var(--color-darkslategray-200);
  display: flex;
  flex-direction: row;
  padding: var(--padding-xs) var(--padding-5xl);
  align-items: center;
  justify-content: center;
  text-align: center;
}
.h24min45sec {
  color: var(--color-whitesmoke);
}
.readyToHarvestContainer {
  position: relative;
  text-align: center;
}
.rectangleParent,
.showAllParent {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: var(--gap-base);
}
.rectangleParent {
  align-self: stretch;
  flex-direction: row;
  justify-content: flex-start;
  font-size: var(--font-size-sm);
  color: var(--color-darkgray);
}
.frameItem {
  align-self: stretch;
  position: relative;
  background-color: var(--color-gray-100);
  height: 1px;
}
.bxsupArrowIcon {
  position: relative;
  width: 12px;
  height: 12px;
  overflow: hidden;
  flex-shrink: 0;
}
.perWeekParent,
.statisticsParent {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.perWeekParent {
  border-radius: var(--br-xs);
  background-color: var(--color-darkslategray-200);
  padding: var(--padding-5xs) var(--padding-xs);
  justify-content: flex-start;
  gap: var(--gap-5xs);
  font-size: var(--font-size-sm);
  color: var(--color-darkgray);
}
.statisticsParent {
  align-self: stretch;
  justify-content: space-between;
  font-size: var(--font-size-lg);
}
.ml {
  position: relative;
  color: var(--color-darkgray);
}
.frameGroup,
.wateringParent {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}
.wateringParent {
  border-radius: var(--br-base);
  background-color: var(--color-gray-200);
  padding: var(--padding-base);
  gap: var(--gap-xs);
}
.frameGroup {
  gap: var(--gap-5xl);
}
.avg60Saturation {
  position: relative;
  font-size: var(--font-size-sm);
  color: var(--color-darkgray);
}
.moistureParent {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-base);
}
.frameInner {
  position: relative;
  background-color: var(--color-darkslategray-100);
  width: 1px;
  height: 227.29px;
}
.p {
  margin: 0;
}
.rectangleGroup {
  width: 40px;
  height: 251.29px;
  flex-direction: column;
  align-items: center;
  gap: var(--gap-xs);
  text-align: center;
}
.frameParent2,
.rectangleContainer,
.rectangleGroup {
  display: flex;
  justify-content: flex-start;
}
.rectangleContainer {
  width: 40px;
  height: 251.29px;
  flex-direction: column;
  align-items: center;
  gap: var(--gap-xs);
}
.frameParent2 {
  margin: 0 !important;
  position: absolute;
  top: 23.72px;
  left: 45.98px;
  flex-direction: row;
  align-items: flex-start;
  gap: var(--gap-7xs);
  z-index: 0;
}
.mon {
  position: relative;
  display: inline-block;
  width: 25px;
  flex-shrink: 0;
}
.frameChild4 {
  position: relative;
  border-radius: var(--br-9xs);
  background-color: var(--color-gainsboro);
  width: 57.8px;
  height: 20px;
}
.monParent {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: var(--gap-5xs);
}
.frameChild10,
.frameChild5,
.frameChild6,
.frameChild7,
.frameChild9 {
  position: relative;
  border-radius: var(--br-9xs);
  background-color: var(--color-gainsboro);
  width: 104.52px;
  height: 20px;
}
.frameChild10,
.frameChild6,
.frameChild7,
.frameChild9 {
  width: 163.98px;
}
.frameChild10,
.frameChild7,
.frameChild9 {
  width: 137.49px;
}
.frameChild10,
.frameChild9 {
  width: 107.26px;
}
.frameChild10 {
  width: 120.09px;
}
.frameParent3 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-xs);
  z-index: 1;
}
.frameParent1 {
  border-radius: var(--br-5xl);
  background-color: var(--color-gray-200);
  display: flex;
  flex-direction: row;
  padding: var(--padding-13xl) var(--padding-53xl) var(--padding-37xl)
    var(--padding-13xl);
  align-items: center;
  justify-content: center;
  position: relative;
  font-size: var(--font-size-3xs);
  color: var(--color-dimgray);
}
.frameDiv {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-5xl);
}
.frameChild16 {
  position: relative;
  border-radius: var(--br-9xs);
  background-color: var(--color-gainsboro);
  width: 140px;
  height: 20px;
}
.frameParent {
  position: absolute;
  top: 0;
  right: -744px;
  background-color: var(--color-gray-400);
  width: 713px;
  height: 1024px;
  display: flex;
  flex-direction: column;
  padding: var(--padding-21xl);
  box-sizing: border-box;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-13xl);
}
.logoChild {
  position: relative;
  width: 28.87px;
  height: 32px;
}
.logo {
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: var(--gap-9xs);
}
.marketplace {
  position: relative;
  color: var(--color-darkgray);
  cursor: pointer;
}
.button {
  border-radius: var(--br-5xs);
  background-color: #222;
  display: flex;
  flex-direction: row;
  padding: var(--padding-5xs) var(--padding-base);
  align-items: flex-start;
  justify-content: flex-start;
}
.icon {
  position: relative;
  width: 24px;
  height: 24px;
  overflow: hidden;
  flex-shrink: 0;
  opacity: 0.9;
}
.buttonParent {
  justify-content: flex-start;
  gap: var(--gap-base);
  font-size: var(--font-size-sm);
  color: var(--color-darkgray);
}
.buttonParent,
.header,
.logoParent {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.header {
  justify-content: flex-start;
  gap: 56px;
  font-size: var(--font-size-base);
}
.logoParent {
  width: 1301px;
  justify-content: space-between;
}
.mintNewPlant {
  position: relative;
  font-size: var(--font-size-base);
  font-weight: 500;
  font-family: var(--font-inter);
  color: var(--color-black);
  text-align: left;
}
.button1,
.yourPlantsGroup {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.button1 {
  cursor: pointer;
  border: 0;
  padding: var(--padding-xs) var(--padding-base);
  background-color: var(--color-mediumspringgreen);
  border-radius: var(--br-xs);
  width: 167px;
  height: 50px;
  box-sizing: border-box;
  justify-content: center;
}
.yourPlantsGroup {
  width: 1301px;
  justify-content: space-between;
  font-size: var(--font-size-13xl);
}
.tab {
  border-radius: var(--br-base);
  background-color: var(--color-gray-500);
  padding: var(--padding-xs) var(--padding-base);
  align-items: flex-start;
  justify-content: flex-start;
}
.tab,
.tab1,
.tabParent {
  display: flex;
  flex-direction: row;
}
.tab1 {
  padding: var(--padding-xs) var(--padding-base);
  align-items: flex-start;
  justify-content: flex-start;
  cursor: pointer;
  color: #888;
}
.tabParent {
  align-items: center;
  justify-content: center;
  gap: var(--gap-xs);
}
.cardMediaIcon {
  align-self: stretch;
  position: relative;
  max-width: 100%;
  overflow: hidden;
  height: 299px;
  flex-shrink: 0;
  object-fit: cover;
}
.nftcodeParent {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  font-size: var(--font-size-sm);
}
.growing2 {
  font-family: var(--font-inter);
}
.span {
  font-size: var(--font-size-mini);
}
.h25mLeft1 {
  font-size: var(--font-size-sm);
}
.h25mLeft {
  font-weight: 500;
  font-family: var(--font-inter);
}
.growing5h25mContainer {
  position: relative;
  color: var(--color-darkgray);
  text-align: left;
}
.button2 {
  cursor: pointer;
  border: 0;
  padding: var(--padding-xs) var(--padding-base);
  background-color: var(--color-darkslategray-200);
  flex: 1;
  border-radius: var(--br-xs);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: var(--gap-5xs);
}
.button2Wrapper,
.card {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}
.button2Wrapper {
  align-self: stretch;
  flex-direction: row;
}
.card {
  flex: 1;
  height: 427px;
  flex-direction: column;
  gap: var(--gap-base);
  cursor: pointer;
}
.growing5h25m {
  position: relative;
  font-size: var(--font-size-sm);
  font-weight: 500;
  font-family: var(--font-inter);
  color: var(--color-darkgray);
  text-align: left;
}
.cardMedia {
  flex: 1;
  height: 427px;
  flex-direction: column;
  gap: var(--gap-base);
}
.cardMedia,
.cardParent,
.frameParent8,
.frameParent9 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}
.cardParent {
  align-self: stretch;
  flex-direction: row;
  gap: var(--gap-5xl);
  font-size: var(--font-size-base);
  color: var(--color-darkgray);
}
.frameParent8,
.frameParent9 {
  flex-direction: column;
}
.frameParent9 {
  width: 1296px;
  gap: var(--gap-13xl);
  font-size: var(--font-size-xl);
}
.frameParent8 {
  position: absolute;
  top: 24px;
  left: 72px;
  gap: 40px;
  font-size: var(--font-size-sm);
}
.growingContainer {
  border-radius: var(--br-xs);
  background-color: var(--color-darkslategray-200);
  display: flex;
  flex-direction: row;
  padding: var(--padding-xs) var(--padding-37xl);
  align-items: center;
  justify-content: center;
  text-align: center;
}
.frameParent10 {
  position: absolute;
  top: 0;
  right: -920px;
  background-color: var(--color-gray-400);
  width: 865px;
  height: 1024px;
  display: flex;
  flex-direction: column;
  padding: var(--padding-21xl);
  box-sizing: border-box;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-13xl);
}
.newPage {
  position: absolute;
  top: -170.03px;
  left: 7177.12px;
  background-color: var(--color-white);
  width: 1440px;
}
.dashboard {
  position: relative;
  background-color: var(--color-gray-300);
  width: 100%;
  height: 1024px;
  overflow: hidden;
  text-align: left;
  font-size: var(--font-size-mini);
  color: var(--color-white);
  font-family: var(--font-inter);
}
`;

// FETCH GROW REGISTRY ABI

const growContract = "0x31D3202d8744B16A120117A053459DDFAE93c855";

const growAbi = fetch(
  "https://raw.githubusercontent.com/8ball030/plantation_station/main/abis/GrowRegistry.json"
);
if (!growAbi.ok) {
  return "Loading";
}

const iface = new ethers.utils.Interface(growAbi.body);

// HELPER FUNCTIONS

const getStakedBalance = (receiver) => {
  const encodedData = iface.encodeFunctionData("balanceOf", [receiver]);

  return Ethers.provider()
    .call({
      to: lidoContract,
      data: encodedData,
    })
    .then((rawBalance) => {
      const receiverBalanceHex = iface.decodeFunctionResult(
        "balanceOf",
        rawBalance
      );

      return Big(receiverBalanceHex.toString())
        .div(Big(10).pow(tokenDecimals))
        .toFixed(2)
        .replace(/\d(?=(\d{3})+\.)/g, "$&,");
    });
};

// DETECT SENDER

if (state.sender === undefined) {
  const accounts = Ethers.send("eth_requestAccounts", []);
  if (accounts.length) {
    State.update({ sender: accounts[0] });
    console.log("set sender", accounts[0]);
  }
}

//if (!state.sender)  return "Please login first";

// FETCH SENDER BALANCE

if (state.balance === undefined && state.sender) {
  Ethers.provider()
    .getBalance(state.sender)
    .then((balance) => {
      State.update({ balance: Big(balance).div(Big(10).pow(18)).toFixed(2) });
    });
}

// FETCH SENDER STETH BALANCE

if (state.stakedBalance === undefined && state.sender) {
  getStakedBalance(state.sender).then((stakedBalance) => {
    State.update({ stakedBalance });
  });
}

// FETCH TX COST

const mintGrow = () => {
  const account = Ethers.provider().getSigner();
  const growRegistry = new ethers.Contract(growContract, growAbi.body, account);

  const hashIPSF = "0x" + "5".repeat(64);
  growRegistry
    .create(state.sender, state.sender, hashIPSF)
    .then((transactionHash) => {
      console.log("transactionHash is " + transactionHash);
    });
};

if (state.txCost === undefined) {
  const gasEstimate = ethers.BigNumber.from(1875000);
  const gasPrice = ethers.BigNumber.from(1500000000);

  const gasCostInWei = gasEstimate.mul(gasPrice);
  const gasCostInEth = ethers.utils.formatEther(gasCostInWei);

  let responseGql = fetch(
    "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: `{
          bundle(id: "1" ) {
            ethPrice
          }
        }`,
      }),
    }
  );

  if (!responseGql) return "";

  const ethPriceInUsd = responseGql.body.data.bundle.ethPrice;

  const txCost = Number(gasCostInEth) * Number(ethPriceInUsd);

  State.update({ txCost: `$${txCost.toFixed(2)}` });
}

// OUTPUT UI

const getSender = () => {
  return !state.sender
    ? ""
    : state.sender.substring(0, 6) +
        "..." +
        state.sender.substring(state.sender.length - 4, state.sender.length);
};

return (
  <Theme>
    <div className="dashboard">
      <div className="badge">
        <div className="div">2</div>
      </div>
      <div className="frameParent">
        <div className="rectangleParent">
          <div className="frameChild" />
          <div className="showAllParent">
            <div className="showAll">Show all</div>
            <div className="plantNameParent">
              <div className="plantName">Plant name</div>
              <div className="x786c65d14c8d137c4b45a8a90d4c2Parent">
                <div className="div">
                  0x786c65d14c8d137c4b45a8a90d4c20d0ca37e5c2
                </div>
                <img className="frameIcon" alt="" src="/frame.svg" />
              </div>
            </div>
            <div className="growingWrapper">
              <div className="growing">{`Growing`}</div>
            </div>
            <div className="readyToHarvestContainer">
              <span>{`Ready to harvest in`}</span>
              <span className="h24min45sec">12h 24min 45sec</span>
            </div>
          </div>
        </div>
        <div className="frameItem" />
        <div className="statisticsParent">
          <div className="div">Statistics</div>
          <div className="perWeekParent">
            <div className="div">Per Week</div>
            <img className="bxsupArrowIcon" alt="" src="/bxsuparrow.svg" />
          </div>
        </div>
        <div className="frameGroup">
          <div className="wateringParent">
            <div className="div">Watering</div>
            <div className="ml">257.14 ml</div>
          </div>
          <div className="wateringParent">
            <div className="div">Lighting</div>
            <div className="ml">4,875 lux</div>
          </div>
        </div>
        <div className="frameGroup">
          <div className="frameDiv">
            <div className="moistureParent">
              <div className="div">Moisture</div>
              <div className="avg60Saturation">Avg. 60% saturation</div>
            </div>
            <div className="frameParent1">
              <div className="frameParent2">
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">
                    <p className="p">{`0%`}</p>
                    <p className="p">Dry</p>
                  </b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">25%</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">50%</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">75%</b>
                </div>
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">
                    <p className="p">100%</p>
                    <p className="p">Saturated</p>
                  </b>
                </div>
              </div>
              <div className="frameParent3">
                <div className="monParent">
                  <b className="mon">MON</b>
                  <div className="frameChild4" />
                </div>
                <div className="monParent">
                  <b className="mon">TUE</b>
                  <div className="frameChild5" />
                </div>
                <div className="monParent">
                  <b className="mon">WED</b>
                  <div className="frameChild6" />
                </div>
                <div className="monParent">
                  <b className="mon">THU</b>
                  <div className="frameChild7" />
                </div>
                <div className="monParent">
                  <b className="mon">FRI</b>
                  <div className="frameChild6" />
                </div>
                <div className="monParent">
                  <b className="mon">SAT</b>
                  <div className="frameChild9" />
                </div>
                <div className="monParent">
                  <b className="mon">SUN</b>
                  <div className="frameChild10" />
                </div>
              </div>
            </div>
          </div>
          <div className="frameDiv">
            <div className="moistureParent">
              <div className="div">Temperature</div>
              <div className="avg60Saturation">Avg. 60% saturation</div>
            </div>
            <div className="frameParent1">
              <div className="frameParent2">
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">0°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">15°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">20°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">25°C</b>
                </div>
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">30°C</b>
                </div>
              </div>
              <div className="frameParent3">
                <div className="monParent">
                  <b className="mon">MON</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">TUE</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">WED</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">THU</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">FRI</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">SAT</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">SUN</b>
                  <div className="frameChild16" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="frameParent8">
        <div className="logoParent">
          <div className="logo">
            <img className="logoChild" alt="" src="/group-2.svg" />
            <div className="div">
              <b>Plantation</b>
              <span>{`Station`}</span>
            </div>
          </div>
          <div className="header">
            <div className="frameGroup">
              <div className="div">Your plants</div>
              <div className="marketplace" onClick={onMarketplaceTextClick}>
                Marketplace
              </div>
            </div>
            <div className="buttonParent">
              <div className="button">
                <div className="growing">Username</div>
              </div>
              <img className="icon" alt="" src="/icon.svg" />
            </div>
          </div>
        </div>
        <div className="yourPlantsGroup">
          <div className="div">Your plants</div>
          {!!state.sender ? (
          <button className="button1" onClick={() => mintGrow()}>
            <div className="mintNewPlant">Mint new plant</div>
          </button>
            ) : (
              <Web3Connect
                className="SubmitContainer"
                connectLabel="Connect with Web3"
              />
            )}
        </div>
        <div className="frameParent9">
          <div className="tabParent">
            <div className="tab">
              <div className="div">Growing plants</div>
            </div>
            <div className="tab1" onClick={onTabContainer1Click}>
              <div className="div">Ready to harvest</div>
            </div>
          </div>
          <div className="cardParent">
            <div className="card" onClick={onCardContainerClick}>
              <img className="cardMediaIcon" alt="" src="/card-media@2x.png" />
              <div className="div">Plant name</div>
              <div className="nftcodeParent">
                <div className="div">0x786c65d....37e5c2</div>
                <div className="div">Show all</div>
              </div>
              <div className="button2Wrapper">
                <button className="button2">
                  <img className="frameIcon" alt="" src="/frame1.svg" />
                  <div className="growing5h25mContainer">
                    <span className="span">
                      <span className="growing2">Growing</span>
                    </span>
                    <span className="h25mLeft">
                      <span className="span">{``}</span>
                      <span className="h25mLeft1">(5h 25m left)</span>
                    </span>
                  </div>
                </button>
              </div>
            </div>
            <div className="cardMedia">
              <img className="cardMediaIcon" alt="" src="/card-media1@2x.png" />
              <div className="div">Plant name</div>
              <div className="nftcodeParent">
                <div className="div">0x786c65d....37e5c2</div>
                <div className="div">Show all</div>
              </div>
              <div className="button2Wrapper">
                <button className="button2">
                  <img className="frameIcon" alt="" src="/frame2.svg" />
                  <div className="growing5h25m">Growing (5h 25m left)</div>
                </button>
              </div>
            </div>
            <div className="cardMedia">
              <img className="cardMediaIcon" alt="" src="/card-media2@2x.png" />
              <div className="div">Plant name</div>
              <div className="nftcodeParent">
                <div className="div">0x786c65d....37e5c2</div>
                <div className="div">Show all</div>
              </div>
              <div className="button2Wrapper">
                <button className="button2">
                  <img className="frameIcon" alt="" src="/frame2.svg" />
                  <div className="growing5h25m">Growing (5h 25m left)</div>
                </button>
              </div>
            </div>
            <div className="cardMedia">
              <img className="cardMediaIcon" alt="" src="/card-media@2x.png" />
              <div className="div">Plant name</div>
              <div className="nftcodeParent">
                <div className="div">0x786c65d....37e5c2</div>
                <div className="div">Show all</div>
              </div>
              <div className="button2Wrapper">
                <button className="button2">
                  <img className="frameIcon" alt="" src="/frame3.svg" />
                  <div className="growing5h25m">Growing (5h 25m left)</div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="frameParent10">
        <div className="rectangleParent">
          <div className="frameChild" />
          <div className="showAllParent">
            <div className="showAll">Show all</div>
            <div className="plantNameParent">
              <div className="plantName">Plant name</div>
              <div className="x786c65d14c8d137c4b45a8a90d4c2Parent">
                <div className="div">
                  0x786c65d14c8d137c4b45a8a90d4c20d0ca37e5c2
                </div>
                <img className="frameIcon" alt="" src="/frame.svg" />
              </div>
            </div>
            <div className="growingContainer">
              <div className="growing">{`Growing`}</div>
            </div>
            <div className="readyToHarvestContainer">
              <span>{`Ready to harvest in`}</span>
              <span className="h24min45sec">12h 24min 45sec</span>
            </div>
          </div>
        </div>
        <div className="frameItem" />
        <div className="statisticsParent">
          <div className="div">Statistics</div>
          <div className="perWeekParent">
            <div className="div">Per Week</div>
            <img className="bxsupArrowIcon" alt="" src="/bxsuparrow.svg" />
          </div>
        </div>
        <div className="frameGroup">
          <div className="wateringParent">
            <div className="div">Watering</div>
            <div className="ml">257.14 ml</div>
          </div>
          <div className="wateringParent">
            <div className="div">Lighting</div>
            <div className="ml">4,875 lux</div>
          </div>
        </div>
        <div className="frameGroup">
          <div className="frameDiv">
            <div className="moistureParent">
              <div className="div">Moisture</div>
              <div className="avg60Saturation">Avg. 60% saturation</div>
            </div>
            <div className="frameParent1">
              <div className="frameParent2">
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">
                    <p className="p">{`0%`}</p>
                    <p className="p">Dry</p>
                  </b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">25%</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">50%</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">75%</b>
                </div>
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">
                    <p className="p">100%</p>
                    <p className="p">Saturated</p>
                  </b>
                </div>
              </div>
              <div className="frameParent3">
                <div className="monParent">
                  <b className="mon">MON</b>
                  <div className="frameChild4" />
                </div>
                <div className="monParent">
                  <b className="mon">TUE</b>
                  <div className="frameChild5" />
                </div>
                <div className="monParent">
                  <b className="mon">WED</b>
                  <div className="frameChild6" />
                </div>
                <div className="monParent">
                  <b className="mon">THU</b>
                  <div className="frameChild7" />
                </div>
                <div className="monParent">
                  <b className="mon">FRI</b>
                  <div className="frameChild6" />
                </div>
                <div className="monParent">
                  <b className="mon">SAT</b>
                  <div className="frameChild9" />
                </div>
                <div className="monParent">
                  <b className="mon">SUN</b>
                  <div className="frameChild10" />
                </div>
              </div>
            </div>
          </div>
          <div className="frameDiv">
            <div className="moistureParent">
              <div className="div">Temperature</div>
              <div className="avg60Saturation">Avg. 60% saturation</div>
            </div>
            <div className="frameParent1">
              <div className="frameParent2">
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">0°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">15°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">20°C</b>
                </div>
                <div className="rectangleContainer">
                  <div className="frameInner" />
                  <b className="div">25°C</b>
                </div>
                <div className="rectangleGroup">
                  <div className="frameInner" />
                  <b className="div">30°C</b>
                </div>
              </div>
              <div className="frameParent3">
                <div className="monParent">
                  <b className="mon">MON</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">TUE</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">WED</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">THU</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">FRI</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">SAT</b>
                  <div className="frameChild16" />
                </div>
                <div className="monParent">
                  <b className="mon">SUN</b>
                  <div className="frameChild16" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="newPage" />
    </div>
  </Theme>
);
