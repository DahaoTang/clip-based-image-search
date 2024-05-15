"use client";

import Image from "next/image";
import { useState } from "react";

export default function Home() {
	const [caption, setCaption] = useState("");
	const [imageIndex, setImageIndex] = useState<string[]>([]);

	// Function to handle form submission
	const handleSubmit = async (e: any) => {
		e.preventDefault();
		console.log("Caption entered: ", caption);

		// Fetch the images based on the entered caption
		const response = await fetch("http://localhost:5001/api/search", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ caption }),
		});

		// Get the images' index data
		const data = await response.json();
		console.log("Index of images found: ", data);
		setImageIndex(data);
	};

	return (
		<div className="w-full h-full text-neutral-700">
			<h1 className="h-[10vh]  flex justify-center items-center">
				<div className="text-center text-2xl">CLIP-based Image Search</div>
			</h1>
			<div className="h-[87vh] flex flex-row">
				<div className="w-[30%] p-5">
					<div className="w-full h-full flex flex-col">
						<form
							onSubmit={handleSubmit}
							className="flex flex-col flex-grow gap-4"
						>
							<textarea
								value={caption}
								onChange={(e) => setCaption(e.target.value)}
								placeholder="Type in caption here"
								className="form-input px-4 py-2 flex-grow border"
							/>
							<button
								type="submit"
								className="border font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline self-end"
							>
								Search for images
							</button>
						</form>
					</div>
				</div>
				<div className="w-[70%] p-5">
					<div className="w-full h-full bg-neutral-50">
						{imageIndex.length > 0 && (
							<div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-6">
								{imageIndex.map(
									(item, index) =>
										index % 5 === 0 && (
											<div
												key={index}
												className="relative group overflow-hidden rounded-lg shadow-lg"
												style={{ height: "200px" }} // Ensure a fixed height for each image's parent div
											>
												<Image
													src={`/${item}`}
													alt={`Image ${index}`}
													fill
													sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw" // Adaptive sizes for responsive images
													className="object-cover transform transition-transform duration-300 group-hover:scale-105"
												/>
											</div>
										)
								)}
							</div>
						)}
					</div>
				</div>
			</div>
			<div className="h-[3vh] text-white flex justify-center items-center">
				<div className="text-neutral-500">
					Developed by{" "}
					<a
						className="underline"
						href="https://dahaotang.com/"
						target="_blank"
						rel="noopener noreferrer"
					>
						Dahao Tang
					</a>
					.&nbsp;2024
				</div>
			</div>
		</div>
	);
}
