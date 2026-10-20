import dayjs from "dayjs";

const clientName = process.env.CLIENT_NAME ?? "a client";
const shootDate = process.env.SHOOT_DATE ?? "2026-12-12";

const daysLeft = dayjs(shootDate).diff(dayjs(), "day");

console.log(`${daysLeft} days until the shoot with ${clientName}`);
