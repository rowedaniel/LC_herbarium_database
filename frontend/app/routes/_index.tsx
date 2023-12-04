import type { MetaFunction, LinksFunction } from "@remix-run/node";
import { Menu } from "~/models/control_menu";
import styleURL from "~/styles/index.css";

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: styleURL },
];
export const meta: MetaFunction = () => {
  return [
    { title: "New Remix App" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  return (
    <div>
      <Menu/>
    </div>
  );
}
